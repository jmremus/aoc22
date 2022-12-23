#--- Day 1: Calorie Counting ---

# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
# they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
# In the example above, this is 24000 (carried by the fourth Elf).
#
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
#
# This time we need the sum of the top 3 elves' calories

import sys

def get_input():
    l = []
    ctr = 1
    cals = (ctr,[])

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for val in f.readlines():
            if val.strip().isdigit():
                cals[1].append(int(val.strip()))
            else:
                l.append(cals)
                ctr+=1
                cals = (ctr,[])
        l.append(cals) 
    return l

def sort_elves(elf):
    return(sum(elf[1]))

def main():
    elves = []
    res = (0,0)

    # let's put the input in a file
    elves = get_input()

    elves = sorted(elves,key=sort_elves)

    print("The top 3 elves are:", elves[-1][0],elves[-2][0],elves[-3][0])
    print("Their calories are:", sum(elves[-1][1]), sum(elves[-2][1]), sum(elves[-3][1]))
    print("The total of the 3 is:", sum(elves[-1][1]) + sum(elves[-2][1]) + sum(elves[-3][1]))

if __name__ == "__main__":
    main()