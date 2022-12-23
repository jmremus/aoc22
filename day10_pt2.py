#! /usr/bin/env python3
# --- Day 10: Cathode-Ray Tube ---

import sys

def get_input():
    instrs = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        instrs = [x.rstrip().split(' ') for x in f.readlines()]
    
    return instrs

def printscr(cyc,X):
    c = cyc % 40
    if c == X or c == X+2 or c == X+1:
        print('#', end='')
    else:
        print('.', end='')
    if cyc % 40 == 0 and cyc > 0:
        print()

def main():

    cyc = 1
    X = 1
    tot = 0
    state = "CONT"
    ins = ["noop"]
    trace_list = [20, 60, 100, 140, 180, 220]

    instrs = get_input()
    printscr(0, 0)
    while len(instrs) > 0:
        if state == "CONT":
            ins = instrs.pop(0)
            
            if ins[0] == "noop":
                pass
            elif ins[0] == "addx":
                state = "addx"
        elif state == "addx":
            X += int(ins[1])
            state = "CONT"
        
        cyc += 1
        printscr(cyc,X)  


if __name__ == "__main__":
    main()