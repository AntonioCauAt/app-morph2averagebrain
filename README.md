<h1 align="center">Morph  to average brain</h1>

<p align="center">
  Morphs MEG/EEG source estimates from an individual brain to the FreeSurfer fsaverage brain with MNE-Python compute_source_morph, and outputs the morphed STC, a plot and a report.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.831"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.831-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Morphs MEG/EEG source estimates from an individual brain to the FreeSurfer fsaverage brain with MNE-Python compute_source_morph, and outputs the morphed STC, a plot and a report.**

Reads left and right hemisphere source estimates, fetches fsaverage into the subject's FreeSurfer directory, computes a source morph from the subject to fsaverage and applies it. Use it to bring individual source estimates into a common space for group analysis. Note: subject_to is not read by main.py; the target is always fsaverage.

| | |
|---|---|
| **Inputs** | `neuro/meeg/stc` · `raw` |
| **Outputs** | `neuro/meeg/stc` · `report/html` · `generic/image/png` |
| **Container** | `brainlife/mne:1.2.1` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.831](https://doi.org/10.25663/brainlife.app.831) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `stc1` | `neuro/meeg/stc` (stc) | yes | Source time course of the subject (left and right hemisphere .stc files). |
| `bem1` | `raw` (bem) | yes | FreeSurfer subject directory of the same subject (with BEM), used as SUBJECTS_DIR. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/stc` | Source estimate morphed to fsaverage (left and right .stc files). |
| `out_dir_report` | `report/html` | HTML report of the morphed source estimate. |
| `out_figs` | `generic/image/png` | Plot of the morphed source estimate. |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `subject_to` | string | `None` | Name of the subject to which to morph as named in the SUBJECTS_DIR. Default is 'fsaverage'. If None, src_to[0]['subject_his_id'] will be used. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.831](https://doi.org/10.25663/brainlife.app.831), choose `neuro/meeg/stc`, `raw` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/stc`, `report/html`, `generic/image/png`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:1.2.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "stc-rh": "/path/to/stc1/stc-rh",
       "stc-lh": "/path/to/stc1/stc-lh",
       "output": "/path/to/bem1/output",
       "subject_to": "None"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Morph  to average brain. brainlife.io App. [doi:10.25663/brainlife.app.831](https://doi.org/10.25663/brainlife.app.831)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7(267):1-13 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Guiomar Niso
- Antonio Caulín

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
