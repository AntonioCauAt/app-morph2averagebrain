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
fname_stcr   = config['stc-rh']
fname_stcl = config ['stc-lh']
subjects_dir = config['output'] 
subject = 'output'

#Copy the two stc files into the same folder
dest_dir = "temp_stc"

os.makedirs(dest_dir, exist_ok=True)

archivo_destino1 = os.path.join(dest_dir, 'inv-rh.stc')
archivo_destino2 = os.path.join(dest_dir, 'inv-lh.stc')

os.system("mv " + fname_stcr + " " + archivo_destino1)
os.system("mv " + fname_stcl + " " + archivo_destino2)


stc = mne.read_source_estimate(dest_dir)
mne.datasets.fetch_fsaverage(subjects_dir=subjects_dir)
morph = mne.compute_source_morph(stc, subject_from=subject,
                                 subject_to='fsaverage',
                                 subjects_dir=subjects_dir)
stc_fsaverage = morph.apply(stc)
#stc_fsaverage.plot(surface='inflated', hemi='both',
#                   subjects_dir=subjects_dir)


fname_stc_average = os.path.join('out_dir', 'inv')
stc_fsaverage.save(fname_stc_average)
# Create and save report
report = mne.Report(title='Morph to Average Brain Report')
#report.add_figs_to_section(fig_stc, 'Source Estimate', section='STC')
report_path = os.path.join('out_dir_report', 'report.html')
report.save(report_path, overwrite=True)
