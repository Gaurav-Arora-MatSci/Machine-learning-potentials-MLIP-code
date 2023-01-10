#!/bin/bash/
path=$(pwd)
dirs=($(find $path -type d))
for dir in "${dirs[@]}"; do
	cd "$dir"
	echo '----------------------------------------'
	pwd
	tail -n 1 job.log
	tail -n 1 *.out
	echo '----------------------------------------'
	cd ..

done
