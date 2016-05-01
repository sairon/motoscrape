#!/bin/sh

# Wrapping script for reporting - usage: reporter.sh from to subject

# Set PYTHONIOENCODING to avoid breaking of the pipes by Unicode chars
PYTHONIOENCODING=UTF-8 ./run.sh 1>report.txt 2>err.txt
if [ $? -eq 0 ]; then
    [ -s report.txt ] && ./sendreport.py -f $1 -t $2 -s $3 report.txt
else
    ./sendreport.py -f $1 -t $2 -s $3 err.txt
fi
