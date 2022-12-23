# --- Day 6: Tuning Trouble ---
#
# Find the first non-duplicating substring 4 chars:
# Here are a few more examples:
#
#    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5

import sys

def get_input():

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    # our input is only one line
    with open(sys.argv[1]) as f:
        for x in f.readlines():
            return x.strip()

def main():
    s = get_input()

    # we are going to forego the two pointer approach
    # since we're guaranteed clean input
    for i in range(0,len(s)):
        x = set(s[i:i+14])
        if len(x) == 14:
            print ("Found marker at position:", i+14)
            return

    
if __name__ == "__main__":
    main()