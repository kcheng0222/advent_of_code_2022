#!/usr/bin/env python3

example = False

if example:
    input_file = "example.txt"
else:
    input_file = "input.txt"
with open(input_file, "r") as f:
    lines = f.read().split("\n\n")

ans = -1

for l in lines:
    temp = 0
    for n in l.strip().split("\n"):
        temp += int(n)
    ans = max(ans, temp)
print(ans)


# part 2

arr = []

for l in lines:
    temp = 0
    for n in l.strip().split("\n"):
        temp += int(n)
    arr.append(temp)

arr.sort(reverse=True)
ans = sum(arr[:3])

print(ans)


