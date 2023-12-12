#!/bin/bash
#SBATCH -J atezo_VHS_1
#SBATCH -p himem
#SBATCH --qos=medium

module purge
ml Anaconda3 && source activate pkaani


python pkaani_loop.py
