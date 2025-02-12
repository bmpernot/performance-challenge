#!/bin/bash

TIMEFORMAT='%R'
times=()
num_runs=5

for ((i=1; i<=num_runs; i++)); do
    echo "Run #$i:"
    time_taken=$({ time docker run --volume "${PWD}/generate/data:/data" proformance-challange/your-name:version-number; } 2>&1 | tail -n 1)
    echo "Execution time: ${time_taken} seconds"
    times+=("$time_taken")
done

total=0
for t in "${times[@]}"; do
    total=$(echo "$total + $t" | bc)
done

average=$(echo "scale=3; $total / $num_runs" | bc)

echo "-----------------------------"
echo "Average execution time: ${average} seconds"
