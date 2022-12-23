#--- Day 1: Calorie Counting ---

# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
# they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
# In the example above, this is 24000 (carried by the fourth Elf).
#
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

import sys

def get_input():
    l = []
    cals = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for val in f.readlines():
            if val.strip().isdigit():
                cals.append(int(val.strip()))
            else:
                l.append(cals)
                cals = []
        l.append(cals) 
    return l

def main():
    elves = []
    res = (0,0)

    # let's put the input in a file
    elves = get_input()

    for elf,v in enumerate(elves):
        if sum(v) > res[1]:
            res = (elf+1,sum(v))

    print("Elf",res[0],"has the most calories:",res[1])
    return res

if __name__ == "__main__":
    main()