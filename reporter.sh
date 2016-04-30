#!/bin/sh

# Wrapping script for reporting - usage: reporter.sh from to

# Set PYTHONIOENCODING to avoid broking of the pipes by Unicode chars
PYTHONIOENCODING=UTF-8 ./run.sh 1>report.txt 2> ./err.txt
if [ $? -eq 0 ]; then
    [ -s report.txt ] && ./sendreport.py $1 $2 report.txt
else
    ./sendreport.py $1 $2 err.txt
fi
