#!/bin/bash

python3 csv_gen.py
python3 manual_read_gen.py
mpirun -np 4 python3 locate.py
