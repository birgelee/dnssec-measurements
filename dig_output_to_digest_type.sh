#!/usr/bin/env bash


cat dig-ds-output.txt | grep "IN\W*DS" | grep "^[^;]" | python3 -u ./get_ds_algo_from_dig_line.py