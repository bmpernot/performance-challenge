#!/bin/bash

TIMEFORMAT='%R'
times=()
num_runs=5

for ((i=1; i<=num_runs; i++)); do
    echo "Run #$i:"
    time_taken=$({ time docker run --gpus all --volume "${PWD}/generate/data:/data" performance-challenge/your-name:version-number; } 2>&1 | tail -n 1)
    # time_taken=$({ time ./src/cuda_log_processor ./generate/data/test_data_input.txt ./generate/data/test_data_output.txt; } 2>&1 | tail -n 1)
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
