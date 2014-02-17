#!/bin/bash
# This script simply runs Python scripts


python=python3.3
echo $#
if [ "$#" -ne 1 ]
then
    echo '$0 <directory>'
    exit 1
fi

find "$1" -name '*.py' -print | xargs -L1 -I {} sh -c "echo '{} '; $python '{}';
echo $?"
