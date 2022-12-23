#!/usr/bin/env python3
#
# --- Day 17: Pyroclastic Flow --- How many units tall will the tower of rocks
# be after 2022 rocks have stopped falling?
#
# Estimate:
#   2022 rocks
#   Avg unit height: (1+3+3+4+2)/5 = 2.6
#   What # of height gained by laying on each type:
#       (1 + 2/3 + (1/3+1/3+1)/3 + 4 2)/5 = 1.6444
#   2022*1.644 = 3324 is est. act is 3068

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
        # 5258 came from the estimate above
        # we are going to make things fall upward, which is weird..
        self.grid = [["." for y in range(0, 7)] for x in range(0, 5258)]
        self.act_h = 1
        self.loffs = 0
        self.instrs = self.get_input()
        self.screen = Screen()
        self.pieces = [[['F', 'F', 'F', 'F']],
                       [[' ', 'P', ' '],
                        ['P', 'P', 'P'],
                        [' ', 'P', ' ']],
                       [[' ', ' ', 'L'],
                        [' ', ' ', 'L'],
                        ['L', 'L', 'L']],
                       [['I'],
                        ['I'],
                        ['I'],
                        ['I']],
                       [['Q', 'Q'],
                        ['Q', 'Q']]]
        # for i in range(0, 10):
        #    for j in range(470, 510):
        #        print(self.grid[i][j], end='')
        #    print()

    def get_input(self):
        if len(sys.argv) < 2:
            print("ERROR: Please provide a filename as input.")
            sys.exit(1)

        # our input is only one line
        with open(sys.argv[1]) as f:
            return list([x.rstrip() for x in f.readlines()][0])

    def print_graph(self):
        for i in range(0, 30):
            if i < self.act_h:
                self.screen.stdscr.addstr(30-i, 15, "|" +
                                          ''.join(self.grid[self.loffs+i]) +
                                          "|")
        self.screen.stdscr.addstr(31, 15, "+-------+")

    def wait_step(self):
        while True:
            c = self.screen.stdscr.getch()
            if c == ord('q'):
                self.screen.quit()
            if c == ord('u'):
                self.loffs += 1
                self.print_graph()
            if c == ord('d'):
                if self.loffs > 0:
                    self.loffs -= 1
                self.print_graph()
            elif c == ord('s'):
                return

    def wait_quit(self):
        while True:
            c = self.screen.stdscr.getch()
            if c == ord('q'):
                self.screen.quit()

    def handle_instr(self, instr):
        lj = len(self.grid[0])
        if instr == '>':
            for i in range(len(self.grid)):
                #first check if we hit and need to stop
                for j in range(lj):
                    if self.grid[i][lj-1-j] == '@':
                        # right edge
                        if lj-1-j+1 == lj:
                            #self.screen.stdscr.addstr(34, 15, "Right Edge           ")
                            return
                        # right edge obstacle
                        if self.grid[i][lj-1-j+1] == '#':
                            #self.screen.stdscr.addstr(34, 15, "Right Obstacle       ")
                            return
                            #self.screen.stdscr.addstr(34, 15, "Moving               ")
            for i in range(len(self.grid)):
                for j in range(lj):
                    if self.grid[i][lj-1-j] == '@':
                        self.grid[i][lj-1-j] = '.'
                        self.grid[i][lj-1-j+1] = '@'

        elif instr == '<':
            #self.screen.stdscr.addstr(34, 15, "Start moving left")
            for i in range(len(self.grid)):
                for j in range(lj):
                    if self.grid[i][j] == '@':
                        # left edge
                        if j == 0:
                            return
                        # left edge obstacle
                        if self.grid[i][j-1] == '#':
                            return
            for i in range(len(self.grid)):
                for j in range(lj):
                    if self.grid[i][j] == '@':
                        self.grid[i][j] = '.'
                        self.grid[i][j-1] = '@'

    def fall(self):
        stop = False
        self.screen.stdscr.addstr(34, 15, "Falling                        ")
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '@':
                    if i == 0:
                        stop = True
                    elif self.grid[i-1][j] == '#':
                        stop = True

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '@':
                    if stop is True:
                        self.grid[i][j] = '#'
                    else:
                        self.grid[i][j] = '.'
                        self.grid[i-1][j] = '@'
        return stop

    def run(self):
        cyc = 0
        piece_cyc = 0
        hrock = 0
        while piece_cyc < 2023:
            #launch block
            block = piece_cyc % 5
            x = self.act_h + 3
            self.act_h = self.act_h + len(self.pieces[block]) + 4
            y = 2
            for i in range(len(self.pieces[block])):
                for j in range(len(self.pieces[block][0])):
                    if self.pieces[block][len(self.pieces[block])-1-i][j] != ' ':
                        self.grid[i+x-1][j+y] = '@'
            #self.screen.stdscr.addstr(32, 15, "Cyc:" + str(cyc))
            #self.screen.stdscr.addstr(33, 15, "Pieces:" + '          ')
            #self.screen.stdscr.addstr(33, 15, "Pieces:" + ''.join(self.pieces[block][0]))

            instr = cyc % len(self.instrs)
            #self.print_graph()
            #self.screen.stdscr.addstr(34, 15, "About to " + self.instrs[instr])
            #self.wait_step()
            self.handle_instr(self.instrs[instr])
            #self.screen.stdscr.addstr(32, 15, "Cyc:" + str(cyc))
            instr = (cyc) % len(self.instrs)
            cyc += 1
            self.print_graph()
            #self.screen.stdscr.addstr(34, 15, "           ")
            #self.wait_step()
            while not self.fall():
                #self.print_graph()
                #self.wait_step()
                self.screen.stdscr.addstr(32, 15, "Cyc:" + str(cyc))
                instr = (cyc) % len(self.instrs)
                #self.screen.stdscr.addstr(34, 15, "About to " + self.instrs[instr])
                self.handle_instr(self.instrs[instr])
                cyc += 1
                self.print_graph()
                if piece_cyc % 100 == 0:
                    self.wait_step()

            self.print_graph()

            #find highest rock:
            for i in range(hrock, len(self.grid)):
                if '#' in self.grid[i]:
                    hrock = i
                else:
                    break
            #self.screen.stdscr.addstr(35, 15, "hrock:" + str(hrock))
            self.act_h = hrock + 2
            piece_cyc += 1

        self.screen.stdscr.addstr(36, 15, "Done!! Height:" + str(hrock))

def main():
    g = Graph()
    g.print_graph()
    g.run()
    #g.wait_pause()
    #g.wait_pause()
    #with open('x','w') as f:
    #    f.write((' '.join(str(s) for s in g.prev) + '\n'))
    g.wait_quit()
if __name__ == "__main__":
    main()
