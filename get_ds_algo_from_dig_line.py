#!/usr/bin/env python3
import fileinput
import sys

total_count = 0
sha2_count = 0

for line in fileinput.input():
    #print(line)
    sline = line.strip()
    if sline == "":
        continue
    split_line = sline.split()
    #print(split_line)
    if len(split_line) < 7:
        continue
    total_count += 1
    if int(split_line[6]) == 2:
        sha2_count += 1
    else:
        print(line, file=sys.stderr)
    print(f"{split_line[0]},{split_line[6]}")


print(f"Of the DS records found: {sha2_count}/{total_count} utilized SHA2.", file=sys.stderr)