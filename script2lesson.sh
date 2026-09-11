#!/bin/bash
read N
for i in $(seq 1 $N)
do
	
	a=$((RANDOM))
	b=$((RANDOM))
	c=$(( a + b ))	
	echo "$a + $b = $c" > "file$i.txt"
done
