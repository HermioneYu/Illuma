#!/bin/bash

FILE_DIR=${HOME}/Illuma/data/*


for file in $FILE_DIR ; do
    fullfilename=$file
    python Task3.py $(basename "$fullfilename") $file

done
