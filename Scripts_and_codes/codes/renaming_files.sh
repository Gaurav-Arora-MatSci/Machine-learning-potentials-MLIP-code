!#/bin/bash

m=10 #Number of files
for ((ivar=1; ivar<=m; ivar+=1))
do
	$ivar-*-OUTCAR OUTCAR-$ivar
done
