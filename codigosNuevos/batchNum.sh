#!/bin/bash
TOT=0
for i in {1..10}
do
  $TOT= $(python3 multNumba.py) 
done
$TOT=$TOT/10
echo $TOT