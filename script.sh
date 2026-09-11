#!/bin/bash
read N
for i in $(seq 0 $N)
do
	a=$RANDOm
	b=$RANDOM 
	c=$(( a + b)) 
	echo $a + $b = $c > file$i.txt 	
done 
