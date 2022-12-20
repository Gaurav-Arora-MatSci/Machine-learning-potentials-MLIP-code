#!/bin/bash
#SBATCH --account=rd-hea
#SBATCH --time=24:00:00
#SBATCH --job-name=mlp_10
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16

#load intel, impi and vasp
module load intel/18.0.1
module load intel-mkl/2020.4.304
module load intel-mpi/2018.2.199

start=$(date +%s.%N)
mlp train init.mtp train.cfg --pot-name=pot.mtp > job.log
duration=$(echo "$(date +%s.%N) - $start" | bc)
echo $duration
echo "Done."

