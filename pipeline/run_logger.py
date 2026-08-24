"""
run_logger.py — audit-grade run logging for the standalone_esd2npz pipeline.

Mirrors the standalone_fitter logging discipline:
  - per-run timestamped output directory
  - run_log.md / run_log.json with status, timing, host, code fingerprints
  - config_snapshot.json capturing every tunable used by the run
  - full console.log tee
  - code_snapshot/ + sha256 of every algorithm file that produced the data
    (the authoritative record of the cut/selection logic)
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

SCHEMA_VERSION = "1.0"

# Algorithm files whose exact content defines the processing (and the cuts).
# Anything listed here is copied verbatim into code_snapshot/ at run start.
CODE_FILES = [
    "src/convert_edm_to_npz.py",
    "src/apply_final_correction.py",
    "src/combine_selection.py",
    "src/local_utils.py",
    "src/esd_to_edm.py",
    "src/list_esd.py",
    "input/correction/correction_api.py",
    "config/paths.py",
    "pipeline/run_all.py",
    "pipeline/cuts_parser.py",
]


def sha256_file(path) -> str:
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return "unavailable"


def _git_info(root: Path) -> dict:
    def _git(*args):
        try:
            return subprocess.run(
                ["git", "-C", str(root), *args], capture_output=True,
                text=True, timeout=10).stdout.strip()
        except Exception:
            return ""
    commit = _git("rev-parse", "HEAD")
    return {
        "git_commit": commit or "not-a-repo",
        "git_branch": _git("rev-parse", "--abbrev-ref", "HEAD"),
        "git_dirty": bool(_git("status", "--porcelain")) if commit else None,
    }


class RunLogger:
    """Context manager that records everything about one pipeline run."""

    def __init__(self, output_dir: Path, project_root: Path,
                 launched_by: str = "script"):
        self.output_dir = Path(output_dir)
        self.project_root = Path(project_root)
        self.launched_by = launched_by
        self.data = {
            "schema_version": SCHEMA_VERSION,
            "run_id": datetime.now().strftime("%Y%m%dT%H%M%S")
                      + "_" + os.urandom(3).hex(),
            "status": "running",
            "launched_by": launched_by,
            "start_utc": datetime.now(timezone.utc).isoformat(),
            "command": " ".join(sys.argv),
            "host": {
                "hostname": socket.gethostname(),
                "user": os.environ.get("USER", ""),
                "platform": platform.platform(),
                "python": sys.version.split()[0],
                "machine": platform.machine(),
            },
            "pipeline": {},      # mode / runs / dirs (filled by run_all)
            "stages": [],        # per-stage records incl. cuts
            "outputs": [],       # deliverable files
        }
        self._t0 = time.time()
        self._fh = None

    # ---------------- console tee ----------------
    class ConsoleTee:
        def __init__(self, stream, logger):
            self.stream, self.logger = stream, logger

        def write(self, text):
            self.stream.write(text)
            if self.logger._fh:
                self.logger._fh.write(text)
                self.logger._fh.flush()
            return len(text)

        def flush(self):
            self.stream.flush()

    def __enter__(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._fh = open(self.output_dir / "console.log", "w")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.data["end_utc"] = datetime.now(timezone.utc).isoformat()
        self.data["elapsed_s"] = round(time.time() - self._t0, 2)
        self.data["status"] = "failed" if exc_type else (
            self.data.get("status", "completed"))
        self.data["host"] = {**self.data["host"], **_git_info(self.project_root)}
        self.dump()
        if self._fh:
            self._fh.close()
        return False

    # ---------------- records ----------------
    def set_pipeline_info(self, **kw):
        self.data["pipeline"].update(kw)

    def add_stage(self, **kw):
        self.data["stages"].append(kw)
        self.dump()

    def add_output(self, path, kind):
        p = Path(path)
        self.data["outputs"].append({
            "kind": kind, "path": str(p),
            "size_bytes": p.stat().st_size if p.exists() else None,
            "sha256": sha256_file(p) if p.exists() else None,
        })

    def dump(self):
        with open(self.output_dir / "run_log.json", "w") as f:
            json.dump(self.data, f, indent=1, ensure_ascii=False)
        with open(self.output_dir / "run_log.md", "w") as f:
            f.write(self._markdown())

    # ---------------- snapshots ----------------
    def snapshot_code(self):
        """Copy algorithm files + hashes: the authoritative cut/provenance record."""
        snap = self.output_dir / "code_snapshot"
        snap.mkdir(parents=True, exist_ok=True)
        hashes = {}
        for rel in CODE_FILES:
            src = self.project_root / rel
            if not src.exists():
                continue
            dst = snap / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())
            hashes[rel] = sha256_file(src)
        with open(snap / "sha256.json", "w") as f:
            json.dump(hashes, f, indent=1)
        return hashes

    def snapshot_config(self, config: dict):
        with open(self.output_dir / "config_snapshot.json", "w") as f:
            json.dump(config, f, indent=1, ensure_ascii=False)

    # ---------------- markdown ----------------
    def _markdown(self) -> str:
        d = self.data
        L = [f"# Run Log — standalone_esd2npz (schema {SCHEMA_VERSION})", "",
             f"**Run ID**: `{d['run_id']}`  |  **Status**: `{d['status']}`  |  "
             f"**Elapsed**: {d.get('elapsed_s','?')} s", "",
             f"**Command**: `{d['command']}`", "",
             "## Pipeline", ""]
        for k, v in d["pipeline"].items():
            L.append(f"- **{k}**: `{v}`")
        L += ["", "## Host", ""]
        for k, v in d["host"].items():
            if v is not None:
                L.append(f"- {k}: `{v}`")
        L += ["", "## Stages", "",
              "| stage | run | status | seconds | detail |",
              "|---|---|---|---|---|"]
        for s in d["stages"]:
            det = s.get("detail", "")
            if isinstance(det, dict):
                det = "; ".join(f"{k}={v}" for k, v in det.items())
            L.append(f"| {s.get('stage','')} | {s.get('run','')} | "
                     f"{s.get('status','')} | {s.get('elapsed_s','')} | {det} |")
        L += ["", "## Outputs", "",
              "| kind | path | size |", "|---|---|---|"]
        for o in d["outputs"]:
            L.append(f"| {o['kind']} | `{o['path']}` | {o['size_bytes']} |")
        L += ["", f"See `code_snapshot/sha256.json` for the exact algorithm "
                  f"versions (cut logic) used by this run, and `cuts/` for the "
                  f"run-specific selection conditions."]
        return "\n".join(L) + "\n"
