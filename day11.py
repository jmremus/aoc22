#!/usr/bin/env python3
# --- Day 11: Monkey in the Middle ---
#
# In this example, the two most active monkeys inspected items 101 and 105
# times. The level of monkey business in this situation can be found by
# multiplying these together: 10605. Figure out which monkeys to chase by
# counting how many items they inspect over 20 rounds. What is the level of
# monkey business after 20 rounds of stuff-slinging simian shenanigans?
import math
import sys

class Monkey:
    def __init__(self, items, opstr, test, mona, monb):
        self.items = items
        self.opstr = opstr
        self.test = test
        self.mona = mona
        self.monb = monb
        self.inspected = 0
    def __repr__(self):
        return f"({self.items},{self.opstr},{self.test},{self.mona},{self.monb},{self.inspected})"
    def __str__(self):
        return f"({self.items},{self.opstr},{self.test},{self.mona},{self.monb},{self.inspected}))"


    def op(self, old):
        new = eval(self.opstr)
        return new

def get_input():
    monkeys = []
    items = []
    opstr = ""
    test = 0
    mona = 0
    monb = 0
    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for x in f.readlines():
            if "Monkey" in x:
                pass
            elif "Starting" in x:
                items = x.split(':')[1].split(',')
                items = [int(y) for y in items]
            elif "Operation" in x:
                opstr = x.replace('  Operation: new = ', '')
            elif "Test" in x:
                test = int(x.replace('Test: divisible by ', ''))
            elif "If true" in x:
                mona = int(x.replace('  If true: throw to monkey ', ''))
            elif "If false" in x:
                monb = int(x.replace('  If false: throw to monkey ', ''))
                monkeys.append(Monkey(items, opstr, test, mona, monb))

    return monkeys

def main():
    monkeys = get_input()

    for i in range(0, 20):
        for monkey in monkeys:
            for j in range(0, len(monkey.items)):
                monkey.inspected += 1
                worry = math.floor(monkey.op(monkey.items[j]) / 3)
                if worry % monkey.test == 0:
                    monkeys[monkey.mona].items.append(worry)
                else:
                    monkeys[monkey.monb].items.append(worry)
            monkey.items = []

    insp = [m.inspected for m in monkeys]
    a = max(insp)
    insp.remove(a)
    b = max(insp)
    print("Score:", a*b)

if __name__ == "__main__":
    main()
