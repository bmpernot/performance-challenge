#!/bin/bash

TIMEFORMAT='It took %R seconds.'
time {
    docker run --gpus all --volume ./test:/data performance-challenge/ben-pernot:2
    # ./src/cuda_log_processor ./test/test_data_input.txt ./test/test_data_output.txt
}

file1="./test/test_data_output.txt"
file2="./test/test_data_expected_output.txt"

checksum1=$(md5sum "$file1" | awk '{ print $1 }')
checksum2=$(md5sum "$file2" | awk '{ print $1 }')

if [ "$checksum1" == "$checksum2" ]; then
  echo "Files are identical."
else
  echo "Files are different."
fi
