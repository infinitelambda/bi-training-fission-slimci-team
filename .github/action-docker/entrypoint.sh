#!/bin/sh -l
echo "Attempting to run the update"
echo $1
echo "adding quotes"
echo \"$1\" > modified_files.txt
echo here
ls -al
pwd
echo "attempting python"
python ./sample_python.py
echo "That ran the python code"