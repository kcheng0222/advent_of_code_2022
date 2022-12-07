#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    input_file = "input.txt"
else:
    input_file = "example.txt"

f = open(input_file, "r")

def get_path(arr, current):
    ''' return array'''
    temp = arr
    for x in current:
        for y in temp:
            if type(y) != int:
                if y["folderName"] == x:
                    temp = y["contents"]
                    break
    return temp

def get_folders(arr, current):
    ret_val = []
    for x in get_path(arr, current):
        if type(x) is dict:
            ret_val.append(x["folderName"])
    return ret_val

arr = [{"folderName": "/", "contents": []}]
current = []

lines = f.readlines()
i = 0

while i < len(lines):
    l = lines[i].strip()
    command = l.split()
    #print("command", l)
    #print("i", i)
    if command[0] == "$":
        currentDir = get_path(arr, current)
        #print("current dir", currentDir)
        if command[1] == "cd":
            if command[2] != "..":
                #print("cd into folder", command[2])
                folder = command[-1]
                current.append(folder)
                currentDir = get_path(arr, current)
                #print("moved. now current is", current)
                #print("currentdir", currentDir)
            elif command[2] == "..":
                #print("POP!")
                current.pop()
            i += 1
        elif command[1] == "ls":
            #print("ls.")
            # list. grab the next files/dirs until "$".
            i += 1
            while i < len(lines) and lines[i][0] != "$":
                #print("i", i)
                entry = lines[i].strip().split()
                #print("ls entry", lines[i].strip())
                if entry[0] == "dir":
                    #print("given a folder.")
                    folder = entry[1]
                    currentFolders = get_folders(arr, current)
                    if folder not in currentFolders:
                        #print("adding dir", folder)
                        currentDir.append({"folderName": folder, "contents": []})
                    else:
                        pass
                        #print(folder, "folder already exists.")
                else:
                    #print("is file. creating file.")
                    size, name = lines[i].strip().split()
                    currentDir.append(int(size))
                i += 1
            #print("DONE WITH LS. MOVING ON TO NEXT COMMAND.")
    #print("now have", arr)
    #print()

ANS = []
folder_sizes = []

def calc_size(arr):
    this_size = 0
    for d in arr:
        if type(d) == int:
            this_size += d
        else:
            #print("in folder", d["folderName"])
            for x in d:
                #print("x", x)
                #if type(x) == int:
                    #this_size += x
                #else:
                if x == "contents":
                    inner_size = calc_size(d[x])
                    folder_sizes.append(inner_size)
                    #print("calculated inner size", inner_size)
                    this_size += inner_size
                    #d["size"] = this_size

    ANS.append(this_size)
    return this_size

calc_size(arr)

temp = 0
for x in ANS:
    if x <= 100000:
        temp += x
print(temp)

    
    
# part 2

folder_sizes.sort()
print(folder_sizes)
need = abs(70000000 - folder_sizes[-1] - 30000000)
print("need", need)
for s in folder_sizes:
    if s >= need:
        # remove s
        print(s)
        break

print("done.")
