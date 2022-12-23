#!/usr/bin/env python3
#
# --- Day 12: Hill Climbing Algorithm ---
#
# Let's do Dijkstra actually

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
        #sys.exit(0)


class Graph:
    def __init__(self):
        self.grid = self.get_input()
        self.dists = [[9999 for y in x] for x in self.grid]
        for i in range(0,len(self.grid)):
            for j in range(0,len(self.grid[0])):
                if self.grid[i][j] == 'S':
                    self.strt = (i, j)
        self.visited = []
        self.use_screen = False
        if self.use_screen:
            self.screen = Screen()
        self.prev = []

        #do two things at once here
        for i, v in enumerate(self.grid):
            for j, y in enumerate(v):
                if y == 'E':
                    self.end = (i, j)
        print("Self.end:", self.end)

    def get_input(self):
        rows = []

        if len(sys.argv) < 2:
            print("ERROR: Please provide a filename as input.")
            sys.exit(1)

        # our input is only one line
        with open(sys.argv[1]) as f:
            rows = [list(x.rstrip()) for x in f.readlines()]
            return rows

    def valid_pt(self, pt, cur_h):
        if pt[0] < 0 or pt[1] < 0:
            return False
        if pt[0] >= len(self.grid) or pt[1] >= len(self.grid[0]):
            return False
        if pt in self.visited:
            return False
        if ord(self.grid[pt[0]][pt[1]]) > cur_h + 1:
            return False
        return True

    def get_nns(self, pt):
        # the height of the current node
        cur_h = self.grid[pt[0]][pt[1]]
        # convert the current height to a number.
        if cur_h == "S":
            cur_h = ord('a')
        else:
            cur_h = ord(cur_h)

        nns = []

        # Temporarily set the end to 'z'
        self.grid[self.end[0]][self.end[1]] = 'z'

        new_pt = (pt[0] + 1, pt[1])
        if self.valid_pt(new_pt, cur_h):
            nns.append(new_pt)
        new_pt = (pt[0], pt[1] + 1)
        if self.valid_pt(new_pt, cur_h):
            nns.append(new_pt)
        new_pt = (pt[0] - 1, pt[1])
        if self.valid_pt(new_pt, cur_h):
            nns.append(new_pt)
        new_pt = (pt[0], pt[1] - 1)
        if self.valid_pt(new_pt, cur_h):
            nns.append(new_pt)

        self.grid[self.end[0]][self.end[1]] = 'E'
        return nns

    def print_graph(self):
        for i, x in enumerate(self.grid):
            self.screen.stdscr.addstr(i, 0, ''.join(x))
    def print_weights(self):
        for i, x in enumerate(self.dists):
            self.screen.stdscr.addstr(i, 0, ''.join(str(x)))

    def wait_step(self):
        while True:
            c = self.screen.stdscr.getch()
            if c == ord('q'):
                self.screen.quit()
            if c == ord('d'):
                self.print_weights()
            elif c == ord('s'):
                return

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

    def h(self, pt):
        import math
        a = (pt[0] - self.end[0])**2
        b = (pt[1] - self.end[1])**2
        return math.sqrt(a + b)

    def reconstruct_path(self, paths, cur):
        tot = []
        i = 0
        while cur != self.strt:
            cur = paths[cur]
            #self.screen.stdscr.addstr(cur[0], cur[1], ".")
            #self.screen.stdscr.addstr(50, 0, "Freal ShortDist:" + str(i))
            i += 1
            #self.wait_step()
            tot.append(cur)
        return tot

    def run(self):
        self.visited.append(self.strt)
        self.prev = []
        self.dists[self.strt[0]][self.strt[1]] = 0
        fscore = [[9999 for y in x] for x in self.grid]
        fscore[self.strt[0]][self.strt[1]] = self.h(self.strt)

        paths = {}
        paths[self.strt] = self.strt
        q = [self.strt]

        if self.use_screen:
            self.screen.stdscr.addstr(50, 0, "Starting")
        while len(q) > 0:
            min_q = q[0]
            # get smallest fscore
            for x in q:
                if fscore[x[0]][x[1]] < fscore[min_q[0]][min_q[1]]:
                    min_q = x
            #self.screen.stdscr.addstr(min_q[0],min_q[1], "X")
            #self.wait_step()
            if min_q == self.end:
                z = self.reconstruct_path(paths, min_q)
                #self.screen.stdscr.addstr(50, 0, "Freal ShortDist:" + str(len(z)))
                self.z = z
                break # reconstruct path

            q.remove(min_q)
            nns = self.get_nns(min_q)
            for n in nns:
                tent_score = self.dists[min_q[0]][min_q[1]] + 1
                if tent_score < self.dists[n[0]][n[1]]:
                    paths[n] = min_q
                    self.dists[n[0]][n[1]] = tent_score
                    fscore[n[0]][n[1]] = tent_score + self.h(n)
                    if n not in q:
                        q.append(n)


def main():
    g = Graph()
    if g.use_screen:
        g.print_graph()
    g.run()
    if g.use_screen:
        g.wait_pause()
        g.wait_quit()
    print(len(g.z))
    with open('x','w') as x:
        g.z.reverse()
        [x.write('(' + str(y[0]) + ',' + str(y[1]) + ')\n') for y in g.z]

if __name__ == "__main__":
    main()
