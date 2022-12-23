#!/usr/bin/env python3

# --- Day 8: Treetop Tree House ---
#
# A tree is visible if all of the other trees between it and an
# edge of the grid are shorter than it. Only consider trees in
# the same row or column; that is, only look up, down, left,
# or right from any given tree.
#
# Consider your map; how many trees are visible from outside the grid?
import sys

def get_input():
    rows = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    # our input is only one line
    with open(sys.argv[1]) as f:
        for x in f.readlines():
            rows.append(x.rstrip())
    return rows

def left(rows, row, col):
    if col == 0:
        return True

    h = rows[row][col]
    i = col-1
    while i >= 0:
        if rows[row][i] >= h:
            return False
        i -= 1

    return True

def right(rows, row, col):
    if col == len(rows[row][col])-1:
        return True

    h = rows[row][col]
    i = col+1
    while i < len(rows[row]):
        if rows[row][i] >= h:
            return False
        i += 1

    return True

def up(rows, row, col):
    if row == 0:
        return True

    h = rows[row][col]
    i = row-1
    while i >= 0:
        if rows[i][col] >= h:
            return False
        i -= 1

    return True

def down(rows, row, col):
    if row == len(rows[row][col])-1:
        return True

    h = rows[row][col]
    i = row+1
    while i < len(rows[row]):
        if rows[i][col] >= h:
            return False
        i += 1

    return True

def main():
    rows = get_input()

    ct = 0

    for row in range(0, len(rows)):
        for col in range(0, len(rows[row])):
            # left
            if left(rows, row, col) is True:
                ct += 1
                continue
            if right(rows, row, col) is True:
                ct += 1
                continue
            if up(rows, row, col) is True:
                ct += 1
                continue
            if down(rows, row, col) is True:
                ct += 1
                continue

    print("Count is:", ct)
if __name__ == "__main__":
    main()
