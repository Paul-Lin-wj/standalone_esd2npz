# Skill: Selection Cuts & Run Archiving (留档) — the most important skill

## Description

How the selection conditions are preserved for every run: what cuts exist,
where their values are archived, and how to read them back. **This is the
core record-keeping skill of the project** — any published number must be
traceable to a `cuts/{R}_cuts.json`.

---

## Two Layers of Cut Provenance

### 1. Runtime cut values — `output/<ts>/cuts/{R}_cuts.json`

Written automatically by `pipeline/cuts_parser.py` from the actual
combine_selection console output of this run. Example (RUN 12370, Ge68):

```json
{
 "run": 12370, "source": "Ge68", "bkg_run": 12419,
 "ROI_MeV": [0.46, 1.23],
 "step1_energy_region_MeV": [0.465, 0.685],
 "z_cut": {"RD_threshold_percent": 0.08, "z_limit_m": 0.4185},
 "z_expected_m": 0.001, "z_source_true_m": 0.0,
 "calib_muonveto_kept": {"kept": 1413255, "total": 1492630, "percent": 94.68},
 "bkg_muonveto_kept":   {"kept": 2612627, "total": 2766750, "percent": 94.43},
 "EFV_selected": {"kept": 109212, "input": 1413255},
 "final_energy_cut_MeV": [0.4945, 0.74526],
 "events_after_ecut": 17407,
 "static_cut_definitions": { ... }
}
```

`cuts/summary.md` accumulates one table row per run for quick multi-run
comparison of cut stability.

### 2. Static cut logic — `code_snapshot/` + `sha256.json`

The hard-coded scan constants (also embedded in the JSON under
`static_cut_definitions` for readability):

| Constant | Value | Meaning |
|---|---|---|
| nominal energies | Ge68 1.022, Cs137 0.662, Mn54 0.835, K40 1.461, Co60 2.506, nH/AmC 2.223, nC 4.94, O16 6.13 MeV | seeds the ROI scan |
| `SOURCE_INITIAL_ROI_SCALE` | Ge68 (0.45, 1.20) MeV | robust initial ROI for edge sources |
| `FIT_LOW/HIGH_SCALE` | 0.9 / 1.1 | final fit window × Step-1 region |
| `FIT_BIN_WIDTH` | 0.002 MeV | fit histogram binning |
| EFV ellipse | `sqrt((ρ/ρ_limit)² + ((z−z_exp)/z_limit)²) ≤ 1` | ρ_limit & z_limit from the robust scan |
| z pre-exclusion | `|z| ≥ 17.7 m` dropped | |
| MuonVeto | keep `MuonVeto == False` | |
| energy cut | `μ ± 3σ` of the fitted peak | σ from Gaussian+poly fit on Step-1 region |

The verbatim `src/combine_selection.py` that produced the cuts is copied into
`output/<ts>/code_snapshot/src/combine_selection.py`, with its sha256 in
`code_snapshot/sha256.json` — the authoritative definition of the cut
algorithm for that run.

## How the Robust Scan Decides the Runtime Values

1. **ROI**: initial window from nominal energy (or `SOURCE_INITIAL_ROI_SCALE`),
   then mu±nσ grid scan with quadratic+Gaussian fits → most stable region
2. **Step-1 energy region**: the robust sub-region used for vertex studies
3. **z_limit**: walking z until the relative derivative drops below the
   0.08 % threshold, confirmed by a 5-point robustness check
4. **ρ_limit / EFV**: ellipse in (ρ, z−z_exp) space with the scanned limits
5. **final energy cut**: Gaussian fit on the Step-1 spectrum → μ±3σ window;
   timestamp files are written with (`Timestamp_Ecut`) and without
   (`Timestamp_wo_Ecut`) this energy cut

## Run Log (audit-grade, mirrors standalone_fitter)

`output/<ts>/run_log.{md,json}`:

- mode, runs, EDM source dir, per-stage status/elapsed
- every deliverable file with size + sha256
- host / python / git commit
- `config_snapshot.json`: every tunable in effect
- `console.log` + `logs/stage*.log`: complete stage output

## Reading Cuts Back Later

```bash
# one run
python -c "import json;print(json.load(open('cuts/12370_cuts.json'))['final_energy_cut_MeV'])"
# all runs
column -t -s'|' cuts/summary.md
```

If you are comparing two processing epochs, diff both the `cuts/*.json`
(values) and `code_snapshot/sha256.json` (logic) — identical hashes with
different values mean input data changed; different hashes mean the cut code
itself changed and results are not comparable without re-audit.
