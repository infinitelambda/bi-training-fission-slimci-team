#!/bin/sh -l
echo "Attempting to run the update"
echo $1
echo "adding quotes"
echo \"$1\" > modified_files.txt
echo here
pwd
ls -al
echo "Envs"
env
echo "attempting python"
python .github/action-docker/sample_python.py
echo "That ran (or not) the python code"
ls -al ~