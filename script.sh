#!/bin/bash
read N
for $(seq 0 <N>)
do
	a=$RANDOm
	b=$RANDOM 
	c=$(( a + b)) 
	touch file$(seq 0 <N>).txt
	echo file$( seq 0 <N>).txt a + b = c	
done 
