# Run Log — standalone_esd2npz (schema 2.0)

**Run ID**: `20260825T082354_bd15af`  |  **Status**: `completed`  |  **Elapsed**: 1240.35 s

**Command**: `run_all.py --runs 12216 12247 12295 12370 9632`

**Exit code**: `0`

## System Information

| Field | Value |
|---|---|
| hostname | `user-Super-Server` |
| user | `lin` |
| platform | `Linux-6.8.0-136-generic-x86_64-with-glibc2.39` |
| python_version | `3.12.3` |
| python_executable | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/.venv/bin/python` |
| timestamp_utc | `2026-08-25T00:23:54.078451+00:00` |

## Code Version

| Field | Value |
|---|---|
| Git commit | `e6442a494f7f47878d22a55852c826aa79b8410e` |
| Git branch | `main` |
| Git has_uncommitted_changes | `True` |

> Warning: Working tree has uncommitted changes.

## Package Versions

- **numpy**: `2.5.2`
- **pandas**: `3.0.5`
- **scipy**: `1.18.1`
- **matplotlib**: `3.11.1`
- **uproot**: `5.7.6`

## Configuration Files

| Config | Path | SHA-256 |
|---|---|---|
| config/paths.py | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/config/paths.py` | `64eb1f8f42d4df00...` |
| requirements.txt | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/requirements.txt` | `06bd0e0e1cbed278...` |
| calib_run_info/calib_to_analyze.txt | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/calib_run_info/calib_to_analyze.txt` | `6cad458da25b8d43...` |
| calib_run_info/CalibRUN_from_file.csv | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/calib_run_info/CalibRUN_from_file.csv` | `84d39f499b8b560a...` |
| input/correction/correction_api.py | `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/input/correction/correction_api.py` | `500d1f45200db7f2...` |

## Pipeline

- **mode**: `from-edm`
- **runs**: `[12216, 12247, 12295, 12370, 9632]`
- **edm_input**: `auto`
- **remote_edm_dir**: `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data`
- **slice**: `None`
- **skip_bkg**: `False`
- **latest_symlink**: `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/latest`
- **latest_target**: `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354`

## Audit (end-of-run completeness)

| Check | Result |
|---|---|
| code/ snapshot files | `41` |
| code all sha256 match | `True` |
| outputs all present | `True` |
| **audit passed** | **`True`** |

## Per-Run Records


### [OK] RUN12204 — bkg-of-12216

| Field | Value |
|---|---|
| Status | ok |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `7` |
| Events (total / finite) | `2875826 / 2875826` |
| Energy min/max | `-999.0 / 52.36014938354492 MeV` |
| Energy mean/median | `-806.0967582843234 / -999.0 MeV` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 105.8 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=7 |
| 2 finalcorrection | ok | 4.9 | phase=3; absolute_scale=0.99743135 |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12204.npz` | npz_raw | `6da51f9bf9d14472...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12204.npz` | npz_corrected | `197193bf0f224acd...` |

### [OK] RUN12216 — Co60

| Field | Value |
|---|---|
| Status | ok |
| run | `12216` |
| source | `Co60` |
| date | `2025-12-15` |
| x_m | `0.0` |
| y_m | `0.0` |
| z_m | `0.0` |
| r_m | `0.0` |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `5` |
| Events (total / finite) | `592021 / 592021` |
| Energy min/max | `-999.0 / 53.19711685180664 MeV` |
| Energy mean/median | `-20.72593733049759 / 0.3787919580936432 MeV` |
| Cuts | `cuts/12216_cuts.json` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 43.5 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=5 |
| 2 finalcorrection | ok | 1.7 | phase=3; absolute_scale=0.99743135 |
| 3 selection | ok | 18.7 | cuts_file=cuts/12216_cuts.json |
| 4 physics-qa | ok | 3.1 |  |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12216.npz` | npz_raw | `a4e7c4023e651fde...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12216.npz` | npz_corrected | `7ad0276aa985740c...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_wo_Ecut/RUN12216.txt` | selection Timestamp_wo_Ecut/RUN12216.txt | `2d241a17de099e99...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12216_EnergySpectrum_Selection.png` | selection figrues_check/Run12216_EnergySpectrum_Selection.png | `ea587c5b45204236...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12216_EnergySpectrum.png` | selection figrues_check/Run12216_EnergySpectrum.png | `fa9547e6c67d6d48...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12216_Rho_vs_Z_EFV.png` | selection figrues_check/Run12216_Rho_vs_Z_EFV.png | `5e147d150da0fba6...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12216_Rho_vs_Z.png` | selection figrues_check/Run12216_Rho_vs_Z.png | `dd4b9700711cfb12...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_Ecut/RUN12216.txt` | selection Timestamp_Ecut/RUN12216.txt | `171a4ff1ae06a008...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12216_2_EnergySpectrum_Fit.png` | selection figures_check_important_new/Run12216_2_EnergySpectrum_Fit.png | `e593e85f33f09e17...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12216_1_SelectionPlot.png` | selection figures_check_important_new/Run12216_1_SelectionPlot.png | `fcf85ec8ee13aebe...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/selection_npz/Run12216_SelectionResult.npz` | selection npz/Run12216_SelectionResult.npz | `317a6e726591fbe0...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12216_physics_qa.png` | physics_qa | `49dd93569224f824...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12216_physics_qa.json` | physics_qa_json | `c1f30256ee52254a...` |

### [OK] RUN12258 — bkg-of-12247

| Field | Value |
|---|---|
| Status | ok |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `8` |
| Events (total / finite) | `3251119 / 3251119` |
| Energy min/max | `-999.0 / 55.16029357910156 MeV` |
| Energy mean/median | `-805.4748574037302 / -999.0 MeV` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 124.3 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=8 |
| 2 finalcorrection | ok | 4.9 | phase=3; absolute_scale=0.99743135 |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12258.npz` | npz_raw | `9effb0de84ec5745...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12258.npz` | npz_corrected | `d6036baa3a7a3191...` |

### [OK] RUN12247 — Mn54

| Field | Value |
|---|---|
| Status | ok |
| run | `12247` |
| source | `Mn54` |
| date | `2025-12-15` |
| x_m | `0.0` |
| y_m | `0.0` |
| z_m | `0.0` |
| r_m | `0.0` |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `3` |
| Events (total / finite) | `518363 / 518363` |
| Energy min/max | `-999.0 / 53.6297607421875 MeV` |
| Energy mean/median | `-24.47321634430217 / 0.3381318747997284 MeV` |
| Cuts | `cuts/12247_cuts.json` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 34.5 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=3 |
| 2 finalcorrection | ok | 1.4 | phase=3; absolute_scale=0.99743135 |
| 3 selection | ok | 16.5 | cuts_file=cuts/12247_cuts.json |
| 4 physics-qa | ok | 3.2 |  |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12247.npz` | npz_raw | `339ac34663929186...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12247.npz` | npz_corrected | `e754a05d2909cbdd...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_wo_Ecut/RUN12247.txt` | selection Timestamp_wo_Ecut/RUN12247.txt | `a09f31ad748a8940...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12247_Rho_vs_Z.png` | selection figrues_check/Run12247_Rho_vs_Z.png | `7ffe00fada8efc37...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12247_EnergySpectrum.png` | selection figrues_check/Run12247_EnergySpectrum.png | `34926862bcd7a3ca...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12247_EnergySpectrum_Selection.png` | selection figrues_check/Run12247_EnergySpectrum_Selection.png | `496d6552015f8bdd...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12247_Rho_vs_Z_EFV.png` | selection figrues_check/Run12247_Rho_vs_Z_EFV.png | `08de6adf2be5a681...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_Ecut/RUN12247.txt` | selection Timestamp_Ecut/RUN12247.txt | `01a82bfaad3ab72d...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12247_1_SelectionPlot.png` | selection figures_check_important_new/Run12247_1_SelectionPlot.png | `5055205d3f4d8269...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12247_2_EnergySpectrum_Fit.png` | selection figures_check_important_new/Run12247_2_EnergySpectrum_Fit.png | `0d3c0d5ed0b6d25a...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/selection_npz/Run12247_SelectionResult.npz` | selection npz/Run12247_SelectionResult.npz | `83ce89e9420ff3c8...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12247_physics_qa.png` | physics_qa | `e79fdc836be5d8a7...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12247_physics_qa.json` | physics_qa_json | `e219770252a85492...` |

### [OK] RUN12306 — bkg-of-12295

| Field | Value |
|---|---|
| Status | ok |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `8` |
| Events (total / finite) | `3603374 / 3603374` |
| Energy min/max | `-999.0 / 63.131629943847656 MeV` |
| Energy mean/median | `-804.281329416384 / -999.0 MeV` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 131.2 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=8 |
| 2 finalcorrection | ok | 5.5 | phase=3; absolute_scale=0.99743135 |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12306.npz` | npz_raw | `93972a99842e74c9...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12306.npz` | npz_corrected | `e3b6ab6475434608...` |

### [OK] RUN12295 — Cs137

| Field | Value |
|---|---|
| Status | ok |
| run | `12295` |
| source | `Cs137` |
| date | `2025-12-16` |
| x_m | `0.0` |
| y_m | `0.0` |
| z_m | `0.0` |
| r_m | `0.0` |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `5` |
| Events (total / finite) | `603907 / 603907` |
| Energy min/max | `-999.0 / 52.74046325683594 MeV` |
| Energy mean/median | `-20.5127816589229 / 0.3909541070461273 MeV` |
| Cuts | `cuts/12295_cuts.json` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 42.5 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=5 |
| 2 finalcorrection | ok | 1.8 | phase=3; absolute_scale=0.99743135 |
| 3 selection | ok | 17.1 | cuts_file=cuts/12295_cuts.json |
| 4 physics-qa | ok | 3.5 |  |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12295.npz` | npz_raw | `8af129eb0b9243e7...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12295.npz` | npz_corrected | `f6f64dc13536175a...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_wo_Ecut/RUN12295.txt` | selection Timestamp_wo_Ecut/RUN12295.txt | `07e91777d197bd9a...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12295_EnergySpectrum_Selection.png` | selection figrues_check/Run12295_EnergySpectrum_Selection.png | `b87d32e51c937671...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12295_Rho_vs_Z.png` | selection figrues_check/Run12295_Rho_vs_Z.png | `62eb76f10652f0d2...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12295_EnergySpectrum.png` | selection figrues_check/Run12295_EnergySpectrum.png | `284423b398ec08cc...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12295_Rho_vs_Z_EFV.png` | selection figrues_check/Run12295_Rho_vs_Z_EFV.png | `25f0f1c758f025da...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_Ecut/RUN12295.txt` | selection Timestamp_Ecut/RUN12295.txt | `b74fa0523303cb9c...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12295_1_SelectionPlot.png` | selection figures_check_important_new/Run12295_1_SelectionPlot.png | `07a8eb075336492d...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12295_2_EnergySpectrum_Fit.png` | selection figures_check_important_new/Run12295_2_EnergySpectrum_Fit.png | `7a4202be6aec458d...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/selection_npz/Run12295_SelectionResult.npz` | selection npz/Run12295_SelectionResult.npz | `57103a9631b0f699...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12295_physics_qa.png` | physics_qa | `b0d2a925f5ff04b5...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12295_physics_qa.json` | physics_qa_json | `2f8b1ab1bb138433...` |

### [OK] RUN12419 — bkg-of-12370

| Field | Value |
|---|---|
| Status | ok |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `7` |
| Events (total / finite) | `2766750 / 2766750` |
| Energy min/max | `-999.0 / 64.24397277832031 MeV` |
| Energy mean/median | `-803.3070719880483 / -999.0 MeV` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 110.2 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=7 |
| 2 finalcorrection | ok | 4.9 | phase=3; absolute_scale=0.99743135 |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12419.npz` | npz_raw | `22fcdc9c52e10672...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12419.npz` | npz_corrected | `8f5c73a6fbf806f8...` |

### [OK] RUN12370 — Ge68

| Field | Value |
|---|---|
| Status | ok |
| run | `12370` |
| source | `Ge68` |
| date | `2025-12-17` |
| x_m | `0.0` |
| y_m | `0.0` |
| z_m | `0.0` |
| r_m | `0.0` |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `8` |
| Events (total / finite) | `1492630 / 1492630` |
| Energy min/max | `-999.0 / 58.23025131225586 MeV` |
| Energy mean/median | `-25.083794602204605 / 0.34133563935756683 MeV` |
| Cuts | `cuts/12370_cuts.json` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 101.9 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=8 |
| 2 finalcorrection | ok | 2.9 | phase=3; absolute_scale=0.99743135 |
| 3 selection | ok | 17.5 | cuts_file=cuts/12370_cuts.json |
| 4 physics-qa | ok | 4.0 |  |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN12370.npz` | npz_raw | `193e9091449e7c45...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN12370.npz` | npz_corrected | `1ac0c20f1ed0a755...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_wo_Ecut/RUN12370.txt` | selection Timestamp_wo_Ecut/RUN12370.txt | `ac4e729fa6dc5930...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12370_EnergySpectrum.png` | selection figrues_check/Run12370_EnergySpectrum.png | `53eced9ad6b9ddd7...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12370_Rho_vs_Z.png` | selection figrues_check/Run12370_Rho_vs_Z.png | `b7440505d4f12385...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12370_Rho_vs_Z_EFV.png` | selection figrues_check/Run12370_Rho_vs_Z_EFV.png | `8263dc0e4e245acf...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12370_EnergySpectrum_Selection.png` | selection figrues_check/Run12370_EnergySpectrum_Selection.png | `10b399b74c19eea5...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_Ecut/RUN12370.txt` | selection Timestamp_Ecut/RUN12370.txt | `8d0d1e1fef4f4ee9...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12370_2_EnergySpectrum_Fit.png` | selection figures_check_important_new/Run12370_2_EnergySpectrum_Fit.png | `c8f4c4ac3ef3bd41...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run12370_1_SelectionPlot.png` | selection figures_check_important_new/Run12370_1_SelectionPlot.png | `63425be27de00743...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/selection_npz/Run12370_SelectionResult.npz` | selection npz/Run12370_SelectionResult.npz | `875b1662638ca16a...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12370_physics_qa.png` | physics_qa | `1bda1b4cf9b13201...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run12370_physics_qa.json` | physics_qa_json | `4acaffc932841412...` |

### [OK] RUN9737 — bkg-of-9632

| Field | Value |
|---|---|
| Status | ok |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `39` |
| Events (total / finite) | `3693643 / 3693643` |
| Energy min/max | `-999.0 / 29.895416259765625 MeV` |
| Energy mean/median | `-798.0925216210604 / -999.0 MeV` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 204.1 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=39 |
| 2 finalcorrection | ok | 5.7 | phase=1; absolute_scale=0.99340419 |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN9737.npz` | npz_raw | `23c205bd1f7b8291...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN9737.npz` | npz_corrected | `1d483e0da7130dee...` |

### [OK] RUN9632 — K40

| Field | Value |
|---|---|
| Status | ok |
| run | `9632` |
| source | `K40` |
| date | `2025-08-25` |
| x_m | `0.0` |
| y_m | `0.0` |
| z_m | `0.0` |
| r_m | `0.0` |
| EDM dir | `/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data` |
| EDM chunks | `19` |
| Events (total / finite) | `2773498 / 2773498` |
| Energy min/max | `-999.0 / 33.88445281982422 MeV` |
| Energy mean/median | `-23.360353099108707 / 0.31189967691898346 MeV` |
| Cuts | `cuts/9632_cuts.json` |

| stage | status | seconds | detail |
|---|---|---|---|
| 1 edm->npz | ok | 184.6 | edm_dir=/lustrefs/juno26/users/zhaorz/Calib/ReProd26B/EDM_from_esd/Data; n_chunks=19 |
| 2 finalcorrection | ok | 4.5 | phase=1; absolute_scale=0.99340419 |
| 3 selection | ok | 17.6 | cuts_file=cuts/9632_cuts.json |
| 4 physics-qa | ok | 5.5 |  |

| output | kind | sha256 |
|---|---|---|
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_raw/RUN9632.npz` | npz_raw | `267b968916f728d6...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/npz_corrected/RUN9632.npz` | npz_corrected | `19600fd42e83b14c...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_wo_Ecut/RUN9632.txt` | selection Timestamp_wo_Ecut/RUN9632.txt | `cf92a9ca670a2dcc...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run9632_EnergySpectrum.png` | selection figrues_check/Run9632_EnergySpectrum.png | `7bec32b971bcbda7...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run9632_Rho_vs_Z_EFV.png` | selection figrues_check/Run9632_Rho_vs_Z_EFV.png | `de99f8d45ad96130...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run9632_Rho_vs_Z.png` | selection figrues_check/Run9632_Rho_vs_Z.png | `9bf9a24a2023096c...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run9632_EnergySpectrum_Selection.png` | selection figrues_check/Run9632_EnergySpectrum_Selection.png | `4cb54935a9ceba34...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/timestamps/Timestamp_Ecut/RUN9632.txt` | selection Timestamp_Ecut/RUN9632.txt | `1402f75027fae7b9...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run9632_2_EnergySpectrum_Fit.png` | selection figures_check_important_new/Run9632_2_EnergySpectrum_Fit.png | `6594afda281f2d93...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/selection/Run9632_1_SelectionPlot.png` | selection figures_check_important_new/Run9632_1_SelectionPlot.png | `a3b9b32ba3b9c95b...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/results/selection_npz/Run9632_SelectionResult.npz` | selection npz/Run9632_SelectionResult.npz | `21da388b126da04f...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run9632_physics_qa.png` | physics_qa | `1f0f5b977a2d0eae...` |
| `/datafs/users/lin/workplace/energy_reco/ENL_agent/standalone_esd2npz/output/20260825_082354/figures/physics_qa/Run9632_physics_qa.json` | physics_qa_json | `330a24554a922659...` |

See `code_snapshot/sha256.json` for the exact algorithm versions (cut logic) used by this run, and `cuts/` for the run-specific selection conditions.
