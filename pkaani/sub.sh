#!/bin/bash
#SBATCH -J conda
#SBATCH -p defq
#SBATCH --qos=medium
#SBATCH --mem=10G

ml Anaconda3/2022.05

conda env create -f pkaani_env.yaml
