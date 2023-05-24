#!/bin/bash

N_EXECUTIONS=10
total_time=0

for ((i=1; i<=N_EXECUTIONS; i++))
do
    start_time=$(date +%s.%N)
    python3 multNumba.py
    end_time=$(date +%s.%N)
    
    execution_time=$(echo "$end_time - $start_time" | bc -l)
    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "$total_time / $N_EXECUTIONS" | bc -l)
echo "Tiempo promedio de ejecución: $average_time segundos"
