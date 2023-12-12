import numpy as np
import pandas as pd
import plotly
import pytraj as pt
from pkaani_mod import calculate_pka

import os

VHS_IDX = 219

def find_VHS_pkas(frames, VHS_IDX, run):
	his_pkas_ensemble = []
	for frame in frames:
		traj = pt.load(f"../run_{run}/gamd.nc", "../atezo_Fab_VHS_LC_pqr_ds.parm7", frame_indices=[frame]).strip(":WAT|:Na+|:Cl-")
		pt.io.write_traj(f"rep_f{frame}.pdb", traj, options="pdbv3", overwrite=True)
	
	pkadict = calculate_pka([f"rep_f{frame}.pdb" for frame in frames], VHS_IDX)

	for frame in frames:
		os.remove(f"rep_f{frame}.pdb")

	for frame in frames:
		with open("c1_pkas.dat", "a") as f:
			f.write(str(pkadict[f"rep_f{frame}.pdb"]) + "\n")
		

c1 = pd.read_csv("cluster1_sample.csv")

for i in c1.to_dict(orient="records"):
	realFrame = i["RunFrame"] + 2000
	realFrameIdx = realFrame - 1
	find_VHS_pkas([realFrameIdx], VHS_IDX, i["Run"])	
