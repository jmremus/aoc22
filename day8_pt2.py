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
        return 1

    score = 0
    h = rows[row][col]
    i = col-1
    while i >= 0:
        score += 1
        if rows[row][i] >= h:
            return score
        i -= 1

    return score

def right(rows, row, col):
    if col == len(rows[row][col])-1:
        return 1

    score = 0
    h = rows[row][col]
    i = col+1
    while i < len(rows[row]):
        score += 1
        if rows[row][i] >= h:
            return score
        i += 1

    return score

def up(rows, row, col):
    if row == 1:
        return 1

    score = 0
    h = rows[row][col]
    i = row-1
    while i >= 0:
        score += 1
        if rows[i][col] >= h:
            return score
        i -= 1

    return score

def down(rows, row, col):
    if row == len(rows[row][col])-1:
        return 1

    score = 0
    h = rows[row][col]
    i = row+1
    while i < len(rows[row]):
        score += 1
        if rows[i][col] >= h:
            return score
        i += 1

    return score

def main():
    rows = get_input()

    score = 0

    for row in range(0, len(rows)):
        for col in range(0, len(rows[row])):
            print("RC is:", row, col)
            l = left(rows, row, col)
            r = right(rows, row, col)
            u = up(rows, row, col)
            d = down(rows, row, col)
            print("..",l,r,u,d)
            temp = l*r*u*d
            if temp > score:
                score = temp

    print("Score is:", score)
if __name__ == "__main__":
    main()
