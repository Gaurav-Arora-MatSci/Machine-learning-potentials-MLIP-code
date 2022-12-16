#!/bin/bash/

mkdir OUTCAR_files_all
n=22
for ((ivar=1; ivar<=n; ivar+=1))
do
	cd $ivar-*/1-*/
	i=$(($ivar+335))
	cp OUTCAR* OUTCAR-$i
	mv OUTCAR-$i ../../OUTCAR_files_all
	cd ../../
done

for ((ivar=1; ivar<=n; ivar+=1))
do
	cd $ivar-*/2-*/
	i=$(($ivar+357))
	cp OUTCAR* OUTCAR-$i
	mv OUTCAR-$i ../../OUTCAR_files_all
	cd ../../
done

for ((ivar=1; ivar<=n; ivar+=1))
do
	cd $ivar-*/3-*/
	i=$(($ivar+379))
	cp OUTCAR* OUTCAR-$i
	mv OUTCAR-$i ../../OUTCAR_files_all
	cd ../../
done