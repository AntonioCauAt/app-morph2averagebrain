# Morph to average brain

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Morphs MEG/EEG source estimates from an individual brain to the FreeSurfer fsaverage brain with MNE-Python compute_source_morph, and outputs the morphed STC, a plot and a report.**

Reads left and right hemisphere source estimates, fetches fsaverage into the subject's FreeSurfer directory, computes a source morph from the subject to fsaverage and applies it. Use it to bring individual source estimates into a common space for group analysis. Note: subject_to is not read by main.py; the target is always fsaverage.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/stc` · `raw` |
| 📤 **Outputs** | `neuro/meeg/stc` · `report/html` · `generic/image/png` |
| 🐳 **Container** | `brainlife/mne:1.2.1` |
| ⚙️ **Resources** | 8 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.831](https://doi.org/10.25663/brainlife.app.831) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `stc1` | `neuro/meeg/stc` (stc) | yes | Source time course of the subject (left and right hemisphere .stc files). |
| `bem1` | `raw` (bem) | yes | FreeSurfer subject directory of the same subject (with BEM), used as SUBJECTS_DIR. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/stc` | Source estimate morphed to fsaverage (left and right .stc files). |
| `out_dir_report` | `report/html` | HTML report of the morphed source estimate. |
| `out_figs` | `generic/image/png` | Plot of the morphed source estimate. |

<details>
<summary><b>⚙️ Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `subject_to` | string | `None` | Name of the subject to which to morph as named in the SUBJECTS_DIR. Default is 'fsaverage'. If None, src_to[0]['subject_his_id'] will be used. |

</details>

📚 **References used by this App:**
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7(267):1-13 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.826-blue.svg)](https://doi.org/10.25663/brainlife.app.826)

This Brainlife app performs morphing of individual source estimates to an average brain using the `mne.compute_source_morph` function. The app aligns individual brain activity data from source estimates, obtained from MEG or EEG inverse solutions, to a common reference brain (such as the Freesurfer "fsaverage" brain).


1) Input file is:
    * `bem` raw data file
    * `stc`  meeg data file

2) Input parameters are:
* `subject_to` Name of the subject to which to morph as named in the SUBJECTS_DIR. Default is 'fsaverage'

3) Ouput files are:
    * Source Time Course (fsaverage)
    * a plot of the STC
    * a html report
   

## Authors
- Guiomar Niso (guiomar.niso@gmail.com)
- Antonio Caulín (antoniocaulinatienzar@gmail.com)

## Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

*- brainlife.io Publishing and Apps:*

Avesani, P., McPherson, B., Hayashi, S. et al. **The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services**. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

*- MNE-Python package:* 

Gramfort A, Luessi M, Larson E, Engemann DA, Strohmeier D, Brodbeck C, Goj R, Jas M, Brooks T, Parkkonen L, and Hämäläinen MS.  **MEG and EEG data analysis with MNE-Python**. Frontiers in Neuroscience, 7(267):1–13, 2013. https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)


#### MIT Copyright (c) 2021 brainlife.io The University of Texas at Austin and Indiana University