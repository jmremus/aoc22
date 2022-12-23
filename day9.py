# --- Day 9: Rope Bridge ---
# Consider a rope with a knot at each end; these knots mark the head and the 
# tail of the rope. If the head moves far enough away from the tail, the tail 
# is pulled toward the head.
# Due to the aforementioned Planck lengths, the rope must be quite short; in
# fact, the head (H) and tail (T) must always be touching (diagonally adjacent 
# and even overlapping both count as touching):
#
# Simulate your complete hypothetical series of motions. How many positions
# does the tail of the rope visit at least once?

import sys

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = x
    def __repr__(self):
        return f"({self.x},{self.y})"
    def __str__(self):
        return f"({self.x},{self.y})"

def get_input():
    rows = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    # our input is only one line
    with open(sys.argv[1]) as f:
        rows = [x.rstrip().split(' ') for x in f.readlines()]
    return rows

# Quite a few valid cases
# 1. H covers T     -> TH   (h2 == t2)
# 2. HT             -> .HT  (h2 == t2)
# 3. HT, move down  -> .T   (h2 != t2), (h1 == t1)
#                      H.
# 4. .T Right       -> .T   (h1 != t1)
#    H.                .H
# 5. .T.. Yank      -> .... (h1 != t1) 
#    ..H.              ..TH
# 6 H moves on to T  -> X   (h2 == t2)
def tense(h1, h2, t1, t2, sign):
    # cases where the head and tail
    # are on the same plane as the movement
    if h2 == t2:
        # Case 1: H Covers T (".X.->.TH")
        if h1 == t1:
            print("Case 1")
            return t1, t2 
        # case 6 
        elif h1 + sign*1 == t1:
            print("Case 6")
            return t1, t2        
        # case 2
        elif abs((h1 + sign*1) - t1) > 1:
            print("Case 2")
            return t1+sign*1, t2
        else:
            print("h2==t2 fell through:",h1,h2,t1,t2,sign*1)             
    else:
        # case 5
        if abs((h1 + sign*1) -t1) > 1:
            print("Case 5")
            return t1 + sign*1,h2
        # remaining cases:
        else:
            print("Remaining cases")
            return t1, t2

def get_dir(dir, h, t):
    if dir == "L":
        return -1, h.x, h.y, t.x, t.y
    elif dir == "R":
        return 1, h.x, h.y, t.x, t.y
    elif dir == "U":
        return 1, h.y, h.x, t.y, t.x
    elif dir == "D":
        return -1, h.y, h.x, t.y, t.x

def move(dir, n, head, tail):
    sign, h1, h2, t1, t2 = get_dir(dir, head, tail)
    vis = []
    
    print("H:",h1,h2,"T:",t1,t2,"sdn", sign, dir, n)
    for i in range(0,n):
        t1, t2 = tense(h1, h2, t1, t2, sign)
        h1 += sign*1
        if dir == "L" or dir == "R":
            head.x = h1
            head.y = h2 
            tail.x = t1
            tail.y = t2
        else:
            head.x = h2
            head.y = h1
            tail.x = t2
            tail.y = t1

        vis.append((tail.x, tail.y))
    print("..vis",vis)
    return head, tail, vis
def main():
    cmds = get_input()
    head = Point()
    tail = Point()
    visited = []

    for cmd in cmds:
        head,tail,vis = move(cmd[0],int(cmd[1]),head,tail)
        visited += vis

    print("Visited:", visited)
    print("Number Visited:", len(set(visited)))

if __name__ == "__main__":
    main()