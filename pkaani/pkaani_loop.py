import numpy as np
import pandas as pd
import plotly
import pytraj as pt
from pkaani_mod import calculate_pka

import os

VHS_IDX = 219
parmFile = "../../atezo_Fab_VHS_LC_pqr_ds.parm7"

def find_VHS_pkas(frames, VHS_IDX, parmFile):
	his_pkas_ensemble = []
	for frame in frames:
		traj = pt.load(f"../gamd.nc", parmFile, frame_indices=[frame]).strip(":WAT|:Na+|:Cl-")
		pt.io.write_traj(f"rep_f{frame}.pdb", traj, options="pdbv3", overwrite=True)
	
		pkadict = calculate_pka([f"rep_f{frame}.pdb"], VHS_IDX)

		with open("pkas.dat", "a") as f:
			f.write(str(pkadict[f"rep_f{frame}.pdb"]) + "\n")
		
		os.remove(f"rep_f{frame}.pdb")
	

find_VHS_pkas(range(99590, 165700, 10), VHS_IDX, parmFile)

