#!/bin/bash
#SBATCH --account=rd-hea
#SBATCH --time=48:00:00
#SBATCH --job-name=mlp
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --mem-per-cpu=8000

#load intel, impi and vasp
module load gcc/12.2.0
module load openmpi/4.1.4

start=$(date +%s.%N)
srun mlp train init.mtp train.cfg --pot-name=pot.mtp > job.log
duration=$(echo "$(date +%s.%N) - $start" | bc)
echo $duration
echo "Done."

