#!/usr/bin/env python3
import sys

file = sys.argv[1]
basefile = file.split(".")[0]

with open(file, "r") as f:
    data = f.readlines()

bin = b""
for line in data:
    line = line.rstrip()
    bin += int.to_bytes(int(line))

with open(basefile + ".bin", "wb") as of:
    of.write(bin)
