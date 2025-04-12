#!/usr/bin/env bash


cat dig-nsec-output.txt | grep "IN\W*NSEC" | python3 -u ./get_nsec_type_from_dig_line.py