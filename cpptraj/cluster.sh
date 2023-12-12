# Created 12/1/23 
# Author: Skanda Sastry
# Purpose: Cluster the frames of a particular VHS+mAb construct using hierarchical agglomerative clustering.
parm ../atezo_Fab_VHS_LC_pqr_ds.parm7
trajin ../run_1/gamd.nc 2001 200000
trajin ../run_2/gamd.nc 2001 200000
trajin ../run_3/gamd.nc 2001 200000
trajin ../run_4/gamd.nc 2001 200000
trajin ../run_5/gamd.nc 2001 200000
autoimage
strip :Na+|:Cl-|:WAT
rms fit :1-432
cluster cl \
 hieragglo epsilon 1.5 clusters 10 averagelinkage \
 rms :219-221&!@H= \
 sieve 10 random \
 out cnumvtime.dat \
 summary summary.dat \
 info info.dat \
 cpopvtime cpopvtime.agr normframe \
 repout rep repfmt pdb \
 singlerepout singlerep.nc singlerepfmt netcdf \
 avgout avg avgfmt pdb
run

