import numpy as np

lines = []
with open("pkas.dat", "r") as f:
	lines = f.readlines()
	lines = [round(float(line[:-1]), 3) for line in lines]
print(np.mean(lines))
print(np.std(lines))
print(lines)
