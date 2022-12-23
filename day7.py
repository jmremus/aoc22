#!/usr/bin/env python3

# --- Day 7: No Space Left On Device ---
#
# Find all of the directories with a total size of at most 100000.
# What is the sum of the total sizes of those directories?

import sys

class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.totsize = 0
        self.parent = None
        self.subdirs = []

def get_input():
    cmds = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    # our input is only one line
    with open(sys.argv[1]) as f:
        for x in f.readlines():
            cmds.append(x.rstrip())
    return cmds

def getroot(pwd):
    while pwd.name != '/':
        pwd = pwd.parent
    return pwd

def cd(cmd, pwd):
    if cmd == "$ cd ..":
        pwd = pwd.parent
        return pwd
    if cmd == "$ cd /":
        pwd = getroot(pwd)
        return pwd
    else:
        dr = Dir(cmd[5:])
        dr.parent = pwd

        if dr not in pwd.subdirs:
            pwd.subdirs.append(dr)

        pwd = dr

    return pwd

def ls(cmds, i, pwd):
    size = 0

    while (i < len(cmds)) and ("$" not in cmds[i]):
        if cmds[i][0] == "d":
            i += 1  # we will see if we can avoid adding this
        else:
            val = cmds[i].split(' ')
            size += int(val[0])
            i += 1

    pwd.size = size
    return i

def replay(cmds,pwd):
    i = 0

    while i < len(cmds):
        if "$ cd" in cmds[i]:
            pwd = cd(cmds[i], pwd)
            i += 1
        elif cmds[i] == "$ ls":
            i += 1
            i = ls(cmds, i, pwd)
        else:
            sys.exit(1)

def find_score(dr):
    l = []

    for d in dr.subdirs:
        if d.totsize == 0:
            l += find_score(d)

    dr.totsize = dr.size
    for d in dr.subdirs:
        dr.totsize += d.totsize

    if dr.totsize <= 100000:
        return l+[dr.totsize]
    else:
        return l

def main():

    dr = Dir("/")

    cmds = get_input()
    replay(cmds, dr)

    print("The sum of DRs under 100k is:", sum(find_score(dr)))

if __name__ == "__main__":
    main()
