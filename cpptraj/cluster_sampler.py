#Created 12/1/2023
# Author: Skanda Sastry
# Purpose: Given a file which has clusters from cpptraj on it (aka a list of frames, and the cluster that
# each frame belongs to) sample from the desired cluster 2500 times. These 2500 frames are fed into 
# pKa-ANI which computes the distribution of pKas over the most energetically favorable GaMD cluster of frames.

import pandas as pd

df = pd.read_csv("cnumvtime.dat", sep="\s+")
f1Count = 163639
f2Count = 80287
f3Count = 80283
f4Count = 80713
f5Count = 84929
CLUSTER = 3

runNum = [1] * f1Count + [2] * f2Count + [3] * f3Count + [4] * f4Count + [5] * f5Count

df["Run"] = runNum

def convert_frame(inFrame, runNum):
	if runNum == 1:
		return inFrame
	elif runNum == 2:
		return inFrame - (f1Count)
	elif runNum == 3:
		return inFrame - (f1Count + f2Count)
	elif runNum == 4:
		return inFrame - (f1Count + f2Count + f3Count)
	elif runNum == 5:
		return inFrame - (f1Count + f2Count + f3Count + f4Count)

conv_frames = []

#for i in df.to_dict(orient="records"):
#	conv_frames.append(convert_frame(i["#Frame"], i["runNum"]))


df["RunFrame"] = df.apply(lambda x: convert_frame(x["#Frame"], x["Run"]), axis=1)

df_c1 = df[df["cl"] == CLUSTER]

df_c1_sample = df_c1.sample(2500)

df_c1_sample.to_csv("cluster_sample.csv")


