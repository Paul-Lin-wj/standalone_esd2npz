# Run Log — standalone_esd2npz (schema 1.0)

**Run ID**: `20260824T182626_b654fb`  |  **Status**: `completed`  |  **Elapsed**: 241.28 s

**Command**: `pipeline/run_all.py`

## Pipeline

- **mode**: `from-edm`
- **runs**: `[12370]`
- **edm_input**: `auto`
- **remote_edm_dir**: `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data`
- **slice**: `None`
- **skip_bkg**: `False`

## Host

- hostname: `user-Super-Server`
- user: `lin`
- platform: `Linux-6.8.0-136-generic-x86_64-with-glibc2.39`
- python: `3.12.3`
- machine: `x86_64`
- git_commit: `ba384df68bb227d2c2e0eb93a0721b9b20b74a20`
- git_branch: `main`
- git_dirty: `True`

## Stages

| stage | run | status | seconds | detail |
|---|---|---|---|---|
| 1 edm->npz | 12370 | ok | 106.1 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data |
| 2 finalcorrection | 12370 | ok | 3.2 | phase=3; absolute_scale=0.99743135 |
| 1 edm->npz | 12419 | ok | 104.6 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data |
| 2 finalcorrection | 12419 | ok | 5.2 | phase=3; absolute_scale=0.99743135 |
| 3 selection | 12370 | ok | 17.5 | cuts_file=cuts/12370_cuts.json |
| 4 physics-qa | 12370 | ok | 3.8 |  |
| publish | - | ok | 0.0 | latest_symlink=/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/latest; target=/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626 |

## Outputs

| kind | path | size |
|---|---|---|
| npz_raw RUN12370 | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/results/npz_raw/RUN12370.npz` | 83330975 |
| npz_corrected RUN12370 | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/results/npz_corrected/RUN12370.npz` | 83330975 |
| npz_raw RUN12419 | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/results/npz_raw/RUN12419.npz` | 154423421 |
| npz_corrected RUN12419 | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/results/npz_corrected/RUN12419.npz` | 154423421 |
| selection Timestamp_wo_Ecut/RUN12370.txt | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/results/timestamps/Timestamp_wo_Ecut/RUN12370.txt` | 2281218 |
| selection figrues_check/Run12370_EnergySpectrum.png | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/selection/Run12370_EnergySpectrum.png` | 88389 |
| selection figrues_check/Run12370_Rho_vs_Z.png | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/selection/Run12370_Rho_vs_Z.png` | 75282 |
| selection figrues_check/Run12370_Rho_vs_Z_EFV.png | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/selection/Run12370_Rho_vs_Z_EFV.png` | 38895 |
| selection figrues_check/Run12370_EnergySpectrum_Selection.png | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/selection/Run12370_EnergySpectrum_Selection.png` | 30759 |
| selection Timestamp_Ecut/RUN12370.txt | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/results/timestamps/Timestamp_Ecut/RUN12370.txt` | 363573 |
| selection figures_check_important_new/Run12370_2_EnergySpectrum_Fit.png | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/selection/Run12370_2_EnergySpectrum_Fit.png` | 247452 |
| selection figures_check_important_new/Run12370_1_SelectionPlot.png | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/selection/Run12370_1_SelectionPlot.png` | 284648 |
| selection npz/Run12370_SelectionResult.npz | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/results/selection_npz/Run12370_SelectionResult.npz` | 2622422 |
| physics_qa | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/physics_qa/Run12370_physics_qa.png` | 378832 |
| physics_qa_json | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260824_182626/figures/physics_qa/Run12370_physics_qa.json` | 624 |

See `code_snapshot/sha256.json` for the exact algorithm versions (cut logic) used by this run, and `cuts/` for the run-specific selection conditions.
