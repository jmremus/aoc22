# --- Day 2: Rock Paper Scissors ---
# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z

# This strategy guide predicts and recommends the following:

#     In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#     In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#     The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?
# A = Rock, B = Paper, and C = Scissors.
# The second column is what you should play in response: X = Rock, Y = Paper, and Z = Scissors.
# The score for a single round is (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
import sys

def get_input():
    rules = []

    if len(sys.argv) < 2:
        print("ERROR: Please provide a filename as input.")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        for val in f.readlines():
            rules.append(val.strip().split(' '))

    return rules

def main():
    score = 0
    
    # it's only 9 permutations, do the whole thing
    judge = { ('A','X') : 4, ('A','Y') : 8, ('A','Z') : 3,
              ('B','X') : 1, ('B','Y') : 5, ('B','Z') : 9,
              ('C','X') : 7, ('C','Y') : 2, ('C','Z') : 6 }

    rules = get_input()

    for r in rules:
        score += judge[(r[0],r[1])]

    print("Score is:", score)
    
    
if __name__ == "__main__":
    main()