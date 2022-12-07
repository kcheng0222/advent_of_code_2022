#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    input_file = "stacks.txt"
    n = 4
else:
    input_file = "stacks_e.txt"
    n = 14

s = open(input_file, "r").readline()

s = s.strip()

for x in range(len(s) - n):
    if len(set(s[x:x+n])) == n:
        print(x+n)
        break


