# --- Day 3: Rucksack Reorganization ---
# To help prioritize item rearrangement, every item type can be converted to a priority:

#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.

# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
import sys

prio_hash = {}

def get_input():
    groups = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    # we are guaranteed % 3
    with open(sys.argv[1]) as f:
        subgrp = []
        i = 0

        for x in f.readlines():
            subgrp.append(x.strip())
            if i % 3 == 2:
                groups.append(subgrp)
                subgrp = []
            i += 1

    #print("Groups are:", groups)
    return groups

def find_dup(x):
    global prio_hash

    hash = {}
    dup = "" 

    for i in x[0]:
        hash[i] = 1
    for i in x[1]:
        if i in hash:
            hash[i] = 2
    for i in x[2]:
        if i in hash and hash[i] == 2:
            dup=i
    #print("Hash is:", hash)
    #print("Dup is:", dup)
    return prio_hash[dup]

def init_prio_hash():
    global prio_hash
    #initialize prio hash
    for i in range(97,123):
        prio_hash[chr(i)] = i-96
        prio_hash[chr(i-32)] = i-70
    #print("prio_hash",prio_hash)

def main():

    groups = get_input()
    init_prio_hash()

    prio = 0
    for x in groups:
        prio += find_dup(x)

    print("The sum of priorities is:", prio)
    
if __name__ == "__main__":
    main()