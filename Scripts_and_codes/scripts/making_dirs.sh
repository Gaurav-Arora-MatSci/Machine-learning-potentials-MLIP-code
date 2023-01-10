#!/bin/bash/

m=5 #number of directories
for ((ivar=1; ivar<=m; ivar+=1))
do
	mkdir $ivar-dir
	cp INCAR POSCAR_*_$ivar POTCAR KPOINTS run_vasp $ivar-dir
	cd $ivar-dir
	mv POSCAR_* POSCAR
	sbatch run_vasp
	cd ..
done

