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

order = "ABC"
order_me = "XYZ"

for l in lines:
    opponent, me = l.split()
    i, j = order.index(opponent)+1, order_me.index(me) + 1
    if i == 1 and j == 3:
        i = 4
    elif i == 3 and j == 1:
        i = -1
    #print("i", i, "j", j)
    if i == j:
        ans += 3 + j
        #print(3 + j)
    elif i < j:
        ans += 6 + j
        #print("won. 6 plus " + str(j))
        #print(6+j)
    else:
        ans += 0 + j
        #print(0+j)
print(ans)
    
# part 2
ans = 0
for l in lines:
    opponent, outcome = l.split()
    i = order.index(opponent)+1
    #print("i", i)
    if outcome == "X":
        #print("lose")
        j = 3 if i == 1 else i-1
        ans += 0 + j
        #print(0+j)
    elif outcome == "Y":
        #print("draw")
        ans += 3 + i
        #print(3+i)
    elif outcome == "Z":
        #print("win")
        j = 1 if i == 3 else i+1
        ans += 6 + j
        #print(6+j)
print(ans)


