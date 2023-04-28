#!/bin/bash
#SBATCH --account=hpt_rad
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=mlp_mpi
#SBATCH --time=08:00:00
#SBATCH --qos=regular

#Load modules
module load intel/19.1.3.304
module load oneapi/2022.2.0
module load mpi/2021.6.0
module load mkl/2022.1.0

start=$(date +%s.%N)
mpirun -n 16 mlp train init.mtp train.cfg --max-iter=10 --pot-name=pot.mtp > job.log
duration=$(echo "$(date +%s.%N) - $start" | bc)
execution_time=`printf "%.2f seconds" $duration`
echo $execution_time
