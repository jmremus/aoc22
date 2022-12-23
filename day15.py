#!/usr/bin/env python3
#
# --- Day 15: Beacon Exclusion Zone --- Consult the report from the sensors you
# just deployed. In the row where y=2000000, how many positions cannot contain
# a beacon?

import re
import sys
import curses


class Screen():
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.start_color()

        self.win = curses.newwin(100, 100, 0, 0)

    def quit(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit(0)


class Graph:
    def __init__(self):
        self.screen = Screen()
        self.sens_beacs = []
        self.get_input()
        print(self.grid_size())
        #    for j in range(470, 510):
        #        print(self.grid[i][j], end='')
        #    print()

    def find_manhattan(self, pair):
        s_x = pair[0][0]
        s_y = pair[0][1]
        b_x = pair[1][0]
        b_y = pair[1][1]

        return abs(s_x - b_x) + abs(s_y - b_y)

    def get_input(self):
        if len(sys.argv) < 2:
            print("ERROR: Please provide a filename as input.")
            sys.exit(1)

        # our input is only one line
        with open(sys.argv[1]) as f:
            for x in f.readlines():
                sensor_x = re.sub('Sensor at x=(-?\\d+),.*', "\\1", x)
                sensor_y = re.sub('.*y=(-?\\d+):.*', "\\1", x)
                beac_x = re.sub('.*beac.*x=(-?\\d+),.*', "\\1", x)
                beac_y = re.sub('.*beac.*x=-?\\d+, y=(-?\\d+)', "\\1", x)
                #print(sensor_x, sensor_y, beac_x, beac_y)
                self.sens_beacs.append([(int(sensor_x), int(sensor_y)),
                                        (int(beac_x), int(beac_y))])

    def solve(self, dest):
        #Plan
        #For each coordinate:
        #0. Make a list range [a+loffs,b+loffs] representing dest row
        #1. Find manhattan distance
        #Find if it projects on to the dest row

        # set up row
        # We need to be really careful with the grid size to take into account:
        # 1. The grid size needs to be double (roffs-loffs + 2) to allow the '#''s to fully expand
        # 2. The left offset is now adds in 'gridsz' which is roffs + loffs + 2
        gs = self.grid_size()
        loffs = gs[0][0]
        roffs = gs[1][1]
        # ROW IS ON THE Y_AXIS
        grid_size = roffs - loffs + 2
        row = ["." for y in range(0, 4*grid_size)]
        print("LEN ROW:", len(row))
        # find all manhattan dists:
        for pair in self.sens_beacs:

            mh = self.find_manhattan(pair)
            # would it touch our row?
            if (pair[0][1] <= dest and pair[0][1]+mh >= dest) \
               or (pair[0][1] >= dest and pair[0][1]-mh <= dest):
                # are we up or down?
                over = 0
                if pair[0][1] >= dest: #below
                    # find overshoot
                    over = abs(pair[0][1]-dest-mh)
                else:
                    over = pair[0][1]+mh-dest
                    # if over = 0 draw '#' over=1 '###' and so on
                row[pair[0][0]-loffs+grid_size] = '#'
                for x in range(over+1):
                    row[pair[0][0]-loffs-x+grid_size] = '#'
                    row[pair[0][0]-loffs+x+grid_size] = '#'

        # Add beacons back in
        for pair in self.sens_beacs:
            if pair[1][1] == dest:
                row[pair[1][0]-loffs+grid_size] = 'B'

        #print("Row is:", ' '.join(row))
        print("Result:", sum([1 for x in row if x == "#"]))
    def grid_size(self):
        min_x = float('inf')
        max_x = float('-inf')
        min_y = float('inf')
        max_y = float('-inf')
        for x in self.sens_beacs:
            #min x
            if x[0][0] < min_x:
                min_x = x[0][0]
            if x[1][0] < min_x:
                min_x = x[1][0]

            # max x
            if x[0][0] > max_x:
                max_x = x[0][0]
            if x[1][0] > max_x:
                max_x = x[1][0]

            if x[0][1] < min_y:
                min_y = x[0][1]
            if x[0][1] > max_y:
                max_y = x[0][1]
            if x[1][1] < min_y:
                min_y = x[1][1]
            if x[1][1] > max_y:
                max_y = x[1][1]
        return [(min_x, min_y), (max_x, max_y)]


def main():
    g = Graph()
    #g.solve(10)
    g.solve(2000000)
    #print(g.sens_beacs[6])
    #print(g.find_manhattan(g.sens_beacs[6]))



if __name__ == "__main__":
    main()
