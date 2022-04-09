#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

file=/tmp/mountain-car-homework_$(uuidgen).py

cp homework.py $file
patch $file solution.patch

PYTHONPATH=$SCRIPT_DIR/src $file

rm $file
