#!/bin/bash/

file="POSCAR" #input which file needs to be grabbed

mkdir $file-files_all
m=10 #Number of folders
n=0 #End number of last OUTCAR/file
for ((ivar=1; ivar<=m; ivar+=1))
do
	cd $ivar-*/1-*/
	i=$(($ivar+$n))
	cp $file* $file-$i
	pwd
	mv $file-$i ../../$file-files_all
	cd ../../
done

for ((ivar=1; ivar<=m; ivar+=1))
do
	cd $ivar-*/2-*/
	i=$(($ivar+$n+$m))
	cp $file* $file-$i
	pwd
	mv $file-$i ../../$file-files_all
	cd ../../
done

for ((ivar=1; ivar<=m; ivar+=1))
do
	cd $ivar-*/3-*/
	i=$(($ivar+$n+$m+$m))
	cp $file* $file-$i
	pwd
	mv $file-$i ../../$file-files_all
	cd ../../
done
