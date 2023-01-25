#!/bin/bash
#SBATCH --account=accel
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=mlp_mpi
#SBATCH --time=08:00:00

#Load modules
module load intel/19.1.3.304
module load oneapi/2022.2.0
module load mpi/2021.6.0
module load mkl/2022.1.0

start=$(date +%s.%N)
mpirun -n 16 lmp_intel_cpu_intelmpi -in run-lammps > job2.log
duration=$(echo "$(date +%s.%N) - $start" | bc)
execution_time=`printf "%.2f seconds" $duration`
echo $execution_time

