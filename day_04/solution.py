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
    j, k = l.strip().split(",")
    a, b = map(int, j.split("-"))
    x, y = map(int, k.split("-"))
    #print(a, b, x, y)
    if a >= x and y >= b:
        #print("yes")
        ans += 1
    elif a <= x and y <= b:
        #print("yes")
        ans += 1
print(ans)

# part 2

ans = 0

for l in lines:
    j, k = l.strip().split(",")
    a, b = map(int, j.split("-"))
    x, y = map(int, k.split("-"))
    #print("a", a, "b", b, "x", x, "y", y)
    if a <= x and x <= b:
        #print("yesa")
        ans += 1
    elif a <= y and y <= b:
        #print("yesb")
        ans += 1
    elif x <= a and a <= y:
        #print("yesc")
        ans += 1
    elif x <= b and b <= y:
        #print("yesd")
        ans += 1
print(ans)




# could have just used in range
