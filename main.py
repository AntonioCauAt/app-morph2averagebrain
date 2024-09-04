# set up environment
import os
import json
import mne

import numpy as np


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)
    
# == CONFIG PARAMETERS ==
fname_stc_rh  = config['stc-rh']
fname_stc_lh  = config['stc-lh']
subjects_dir  = config['output'] 

subject = 'output'


# == MORPH TO AVERAGE BRAIN ==

# Get fsaverage template
mne.datasets.fetch_fsaverage(subjects_dir=subjects_dir)

# Read STC files
# You read stc files from right and left hemispheres at once
# if you provide the "base part" of the path, without the -lh.stc or -rh.stc
# MNE-Python will then try to read the data for both hemispheres from disk
stc = mne.read_source_estimate(fname_stc_rh[:-7])

# Compute and apply morphing
morph = mne.compute_source_morph(stc, subject_from=subject,
                                 subject_to='fsaverage',
                                 subjects_dir=subjects_dir)

stc_fsaverage = morph.apply(stc)

# FIGURES
#stc_fsaverage.plot(surface='inflated', hemi='both',
#                   subjects_dir=subjects_dir)


# SAVE STC
fname_stc_fsaverage = os.path.join('out_dir', 'inv')
stc_rh_fsaverage.save(fname_stc_fsaverage)

# Create and save report
report = mne.Report(title='Morph to Average Brain Report')
#report.add_figs_to_section(fig_stc, 'Source Estimate', section='STC')
report_path = os.path.join('out_dir_report', 'report.html')
report.save(report_path, overwrite=True)

