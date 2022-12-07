#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    input_file = "stacks.txt"
    instructions = open("instructions.txt", "r").readlines()
    n = 9
else:
    input_file = "stacks_e.txt"
    instructions = open("instructions_e.txt", "r").readlines()
    n = 3

lines = open(input_file, "r").readlines()

# part 1

ans = 0

stacks = [[] for _ in range(n)]

for l in lines:
    l = l.rstrip()
    i = 0
    for stack in range(n):
        c = l[i+1:i+2]
        #print("c", c)
        i += 4
        if c and not c.isspace():
            #print("adding", c, "to stack", stack)
            stacks[stack] = [c] + stacks[stack]
print("stacks", stacks)

for i in instructions:
    arr = i.strip().split()
    count, source, destination = map(int, [arr[1], arr[3], arr[5]])
    source -= 1
    destination -= 1
    #print(source, destination)
    #print("removing from", stacks[source])
    for _ in range(count):
        stacks[destination].append(stacks[source].pop())
    #print("done")
#print(stacks)

ans = ""

for x in stacks:
    ans += x[-1]
print(ans)


# part 2

stacks = [[] for _ in range(n)]

for l in lines:
    l = l.rstrip()
    i = 0
    for stack in range(n):
        c = l[i+1:i+2]
        #print("c", c)
        i += 4
        if c and not c.isspace():
            #print("adding", c, "to stack", stack)
            stacks[stack] = [c] + stacks[stack]
print("stacks", stacks)


for i in instructions:
    arr = i.strip().split()
    count, source, destination = map(int, [arr[1], arr[3], arr[5]])
    source -= 1
    destination -= 1
    moving = stacks[source][-count:]
    #print("moving", moving)
    stacks[source] = stacks[source][:-count]
    stacks[destination] += moving
    #print(stacks)
    #print(source, destination)
    #print("removing from", stacks[source])
    #print("done")
#print(stacks)

ans = ""

for x in stacks:
    ans += x[-1]
print(ans)

