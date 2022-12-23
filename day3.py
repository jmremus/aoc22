# --- Day 3: Rucksack Reorganization ---
# To help prioritize item rearrangement, every item type can be converted to a priority:

#     Lowercase item types a through z have priorities 1 through 26.
#     Uppercase item types A through Z have priorities 27 through 52.

# In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
import sys

prio_hash = {}

def get_input():
    sacks = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        sacks = [val.strip() for val in f.readlines()]

    return sacks

def find_dup(x):
    global prio_hash

    # we know x is even
    a = x[0:int(len(x)/2)]
    b = x[int(len(x)/2):]

    hash = {}
    dup = "" 

    for i in a:
        hash[i] = True

    for i in b:
        if i in hash:
            dup = i
            break

    return prio_hash[i]

def init_prio_hash():
    global prio_hash
    #initialize prio hash
    for i in range(97,123):
        prio_hash[chr(i)] = i-96
        prio_hash[chr(i-32)] = i-70
    print("prio_hash",prio_hash)

def main():

    sacks = get_input()
    init_prio_hash()

    prio = 0
    for x in sacks:
        prio += find_dup(x)

    print("The sum of priorities is:", prio)
    
if __name__ == "__main__":
    main()