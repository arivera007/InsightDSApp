#!/usr/bin/env bash

# Author: Adriana Rivera
# Located in https://github.com/arivera007/InsightDSApp

# next I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/frequency.py
chmod a+x ./src/runningMedian.py

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python3 ./src/frequency.py ./wc_input ./wc_output/wc_result.txt
python3 ./src/runningMedian.py ./wc_input ./wc_output/med_result.txt