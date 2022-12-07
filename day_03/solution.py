#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    input_file = "input.txt"
else:
    input_file = "example.txt"

with open(input_file, "r") as f:
    lines = f.readlines()

# part 1

ans = 0
for l in lines:
    l = l.strip()
    n = len(l) // 2
    a, b = l[:n], l[n:]
    c = list(set(a).intersection(b))[0]
    #print(c)
    if ord(c) < 97:
        ans += ord(c) - 38
        #print(ord(c)-38)
    else:
        #print(ord(c)-96)
        ans += ord(c) - 96
print(ans)

# part 2

ans = 0
i = 0
while i < len(lines):
    arr = []
    for x in range(3):
        arr.append(set(lines[i].strip()))
        i += 1
    c = list(arr[0].intersection(arr[1]).intersection(arr[2]))[0]
    #print(c)
    #print(c)
    if ord(c) < 97:
        ans += ord(c) - 38
        #print(ord(c)-38)
    else:
        #print(ord(c)-96)
        ans += ord(c) - 96
print(ans)
