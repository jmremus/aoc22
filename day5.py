# --- Day 5: Supply Stacks ---

# The Elves just need to know which crate will end up on top of each stack; in this example, 
# the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these 
# together and give the Elves the message CMZ.
# After the rearrangement procedure completes, what crate ends up on top of each stack?

import sys
from collections import defaultdict, deque

def get_input():
    stack = []
    moves = []
    nums = ""
    num_stacks = 0
    algn = 0

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    # this will be kind of tricky
    # we need
    # 1. # of stacks
    # 2. the moves
    # 3. What's in each stack
    # Let's just start by separating the strings
    with open(sys.argv[1]) as f:
        for x in f.readlines():
            if 'move' in x:
                moves.append(x.strip('\n'))
            elif '[' in x:
                stack.append(x.rstrip())
            elif " 1" in x:
                nums = x.strip('\n')
    
    num_stacks = int(max(nums.split(' ')))
    algn = nums.index("1")
    print("ALGN is:",algn)
    stackd = defaultdict(deque)
    for s in stack:
        for i in range(0,num_stacks):
            offs = algn+4*i
            print("Assigning stack:", i+1, "From:", s, s[0], s[1], s[2])
            if len(s) > offs and s[offs].isalpha():
                stackd[i+1].appendleft(s[offs])
                print("Stackd[1]",stackd[i+1])

    moves_parsed = []
    for s in moves:
        a=s.split(" from ")
        b=a[1].split(" to ")
        c=a[0].split("move ")
        moves_parsed.append([int(c[1]),int(b[0]),int(b[1])])
    
    print_stacks(stackd)

    return num_stacks,stackd,moves_parsed

def print_stacks(st):
    print("PRINTING STACKS...")
    for k,v in st.items():
        print("Stack #:",k,"Contents: ", v)
    print("Done...")

def main():
    num,stacks,moves = get_input()
    print_stacks(stacks)

    for move in moves:
        print("Move is:", move, stacks[move[1]], stacks[move[2]])
        for x in range(0,move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
            print_stacks(stacks)

    print_stacks(stacks)
    peeks = ""

    for i in range(1,num+1):
        peeks += stacks[i].pop()

    print("Last ones are:",peeks)

    return

if __name__ == "__main__":
    main()