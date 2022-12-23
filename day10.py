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

def trace(cyc,X):
    print("cyc, X, cyc*X:", cyc, X, cyc*X)

    return cyc*X

def main():

    cyc = 1
    X = 1
    tot = 0
    state = "CONT"
    ins = ["noop"]
    trace_list = [20, 60, 100, 140, 180, 220]

    instrs = get_input()

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
        if cyc in trace_list:
            tot += trace(cyc,X)  

    print("Total is:", tot)

if __name__ == "__main__":
    main()