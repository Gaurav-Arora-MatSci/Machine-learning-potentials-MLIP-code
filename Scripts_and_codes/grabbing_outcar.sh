#!/bin/bash/

mkdir OUTCAR_files
n=14
for ((ivar=0; ivar<=n; ivar+=1))
do
	cd POSCAR_$ivar
	cp OUTCAR OUTCAR-$ivar
	mv OUTCAR-$ivar ../OUTCAR_files
	cd ..
done


