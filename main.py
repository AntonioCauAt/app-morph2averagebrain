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
# Since you can't read stc files from right and left hemispheres at once
# We load and morph them separately
stc_rh = mne.read_source_estimate(fname_stc_rh)
stc_lh = mne.read_source_estimate(fname_stc_lh)

# Compute and apply morphing
morph_rh = mne.compute_source_morph(stc_rh, subject_from=subject,
                                 subject_to='fsaverage',
                                 subjects_dir=subjects_dir)
morph_lh = mne.compute_source_morph(stc_lh, subject_from=subject,
                                 subject_to='fsaverage',
                                 subjects_dir=subjects_dir)
stc_rh_fsaverage = morph_rh.apply(stc_rh)
stc_lh_fsaverage = morph_lh.apply(stc_lh)

# FIGURES
#stc_fsaverage.plot(surface='inflated', hemi='both',
#                   subjects_dir=subjects_dir)


# SAVE STC
fname_stc_rh_fsaverage = os.path.join('out_dir', 'inv-rh.stc')
fname_stc_lh_fsaverage = os.path.join('out_dir', 'inv-lh.stc')

stc_rh_fsaverage.save(fname_stc_rh_fsaverage)
stc_lh_fsaverage.save(fname_stc_lh_fsaverage)

# Create and save report
report = mne.Report(title='Morph to Average Brain Report')
#report.add_figs_to_section(fig_stc, 'Source Estimate', section='STC')
report_path = os.path.join('out_dir_report', 'report.html')
report.save(report_path, overwrite=True)

