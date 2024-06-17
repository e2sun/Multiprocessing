#!/bin/bash
#SBATCH --job-name=Testing
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-4
#SBATCH -n 16

echo "python3 TextFiles.py -n $1"
python3 TextFiles.py -n $1 