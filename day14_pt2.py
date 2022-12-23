#!/usr/bin/env python3
#
# --- Day 14: Regolith Reservoir ---
# Let's make a falling sand simulator

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
        # initialize points to "."
        # We'll do 1k by 1k
        # Really the screen will cover (450 550) (0 100)
        self.grid = [["." for y in range(0, 1000)] for x in range(0, 180)]
        self.grid[0][500] = '+'
        #self.screen = Screen()
        self.get_input()
        self.draw_floor()
        # for i in range(0, 10):
        #    for j in range(470, 510):
        #        print(self.grid[i][j], end='')
        #    print()

    def draw_floor(self):
        min_y = 0
        for i in range(1, len(self.grid)):
            if '#' in self.grid[i]:
                min_y = i

        min_y += 2
        #print("min_y is:", min_y)
        for i in range(0, len(self.grid[0])):
            self.grid[min_y][i] = '#'

    def draw_line(self, pt1, pt2):
        if pt1[0] == pt2[0]:
            for i in range(min(pt1[1], pt2[1]), max(pt2[1], pt1[1]) + 1):
                self.grid[i][pt1[0]] = '#'
                #print("# at:", pt1[0],i)
        else:
            for i in range(min(pt1[0], pt2[0]), max(pt1[0], pt2[0]) + 1):
                self.grid[pt1[1]][i] = '#'

    def get_input(self):
        if len(sys.argv) < 2:
            print("ERROR: Please provide a filename as input.")
            sys.exit(1)

        # our input is only one line
        with open(sys.argv[1]) as f:
            for x in f.readlines():
                coords = x.split(' -> ')
                for i in range(1, len(coords)):
                    pt1 = [int(y) for y in coords[i-1].split(",")]
                    pt2 = [int(y) for y in coords[i].split(",")]
                    self.draw_line(pt1, pt2)

    def print_graph(self):
        for i in range(0, 30):
            self.screen.stdscr.addstr(i, 0, ''.join(self.grid[i][450:550]))

    def wait_step(self):
        pass
        # while True:
        #     c = self.screen.stdscr.getch()
        #     if c == ord('q'):
        #         self.screen.quit()
        #     if c == ord('d'):
        #         self.print_weights()
        #     elif c == ord('s'):
        #         return

    def wait_pause(self):
        while True:
            c = self.screen.stdscr.getch()
            if c == ord('q'):
                return

    def wait_quit(self):
        while True:
            c = self.screen.stdscr.getch()
            if c == ord('q'):
                self.screen.quit()

    def launch_sand(self):
        """Return True if we fell off, else False to launch more sand"""
        #start just below launch point
        sand = [0, 500]
        while True:
            # 1. did we hit the bottom?
            if len(self.grid) == sand[0]+1:
                return True
            # 2. Did we hit a barrier?
            #elif self.grid[sand[0]+1][sand[1]] == '#':
            #    return False
            # 3. Did we hit sand?
            elif self.grid[sand[0]+1][sand[1]] == 'o' or self.grid[sand[0]+1][sand[1]] == '#':
                # 3a moving left, do we fall off
                if sand[1]-1 < 0:
                    print("no left")
                    return True
                # 3b moving left do we hit a wall or sand?
                elif self.grid[sand[0]+1][sand[1]-1] != '#' and self.grid[sand[0]+1][sand[1]-1] != 'o':
                    self.grid[sand[0]][sand[1]] = '.'
                    self.grid[sand[0]+1][sand[1]-1] = 'o'
                    #if sand[0]+1 <= 30 and sand[1] < 550 and sand[1] > 450:
                    #    self.screen.stdscr.addstr(sand[0], sand[1]-450, '.')
                    #    self.screen.stdscr.addstr(sand[0]+1, sand[1]-1-450, 'o')
                    sand[0] += 1
                    sand[1] = sand[1] - 1
                    self.wait_step()
                    continue
                    #return False
                # 3c moving right do we fall off?
                if sand[1]+1 == len(self.grid[0]):
                    return True
                # 3d moving right do we hit a wall or sand?
                elif self.grid[sand[0]+1][sand[1]+1] != '#' and self.grid[sand[0]+1][sand[1]+1] != 'o':
                    self.grid[sand[0]][sand[1]] = '.'
                    self.grid[sand[0]+1][sand[1]+1] = 'o'
                    #if sand[0]+1 <= 30 and sand[1] < 550 and sand[1] > 450:
                    #    self.screen.stdscr.addstr(sand[0], sand[1]-450, '.')
                    #    self.screen.stdscr.addstr(sand[0]+1, sand[1]+1-450, 'o')
                    sand[0] += 1
                    sand[1] = sand[1] + 1
                    self.wait_step()
                    continue
                    #return False
                else:
                    # we're stuck
                    if sand[0] == 0 and sand[1] == 500:
                        return True
                    return False
            # 4. Fall down
            else:
                self.grid[sand[0]][sand[1]] = '.'
                self.grid[sand[0]+1][sand[1]] = 'o'
                #print("sand[0]",sand[0],sand[1])
                #if sand[0]+1 <= 30 and sand[1] < 550 and sand[1] > 450:
                #    self.screen.stdscr.addstr(sand[0], sand[1]-450, '.')
                #    self.screen.stdscr.addstr(sand[0]+1, sand[1]-450, 'o')
                sand[0] = sand[0] + 1
                continue

            self.wait_step()

            print("returning kindly")
    def run(self):
        done = False

        while not done:
            done = self.launch_sand()
        #self.screen.stdscr.addstr(30, 0, "Done")
        s = 0
        for x in self.grid:
            for y in x:
                if y == 'o':
                    s += 1
        s -= 1
        #self.screen.stdscr.addstr(30, 0, "X is:" + str(s))
        print("X is:", s+2)

def main():
    g = Graph()
    #g.print_graph()
    g.run()
    #g.wait_pause()
    #g.wait_pause()
    #with open('x','w') as f:
    #    f.write((' '.join(str(s) for s in g.prev) + '\n'))
    #g.wait_quit()
if __name__ == "__main__":
    main()
