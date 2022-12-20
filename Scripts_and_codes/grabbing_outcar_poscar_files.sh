#!/bin/bash/

mkdir POSCAR_files_all
m=10 #Number of folders
n=27 #End number of last OUTCAR/POSCAR
for ((ivar=1; ivar<=m; ivar+=1))
do
	cd $ivar-*/1-*/
	i=$(($ivar+$n))
	cp POSCAR* POSCAR-$i
	pwd
	mv POSCAR-$i ../../POSCAR_files_all
	cd ../../
done

for ((ivar=1; ivar<=m; ivar+=1))
do
	cd $ivar-*/2-*/
	i=$(($ivar+$n+$m))
	cp POSCAR* POSCAR-$i
	pwd
	mv POSCAR-$i ../../POSCAR_files_all
	cd ../../
done

for ((ivar=1; ivar<=m; ivar+=1))
do
	cd $ivar-*/3-*/
	i=$(($ivar+$n+$m+$m))
	cp POSCAR* POSCAR-$i
	pwd
	mv POSCAR-$i ../../POSCAR_files_all
	cd ../../
done
