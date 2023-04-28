#!/bin/bash/

n=14
for ((ivar=0; ivar<=n; ivar+=1))
do
	mlp convert-cfg OUTCAR-$ivar temp.txt --input-format=vasp-outcar --last
	cat temp.txt >> train.cfg
done

rm temp.txt


