"""
R = Rock
P = paper
S = Scissors

count => wins losses and ties
"""


# import libraries

import random
import sys


# print welcome message and declare variables

print("#####################################")
print("#####          Welcome          #####")
print("#####            TO             #####")
print("#####    ROCK, PAPER, SCISSORS  #####")
print("#####           GAME            #####")
print("#####################################")

wins = 0
losses = 0
ties = 0
count = 0

while True:     # main loop
    print('\n%s Wins, %s Losses, %s Ties' %(wins, losses, ties))

    while True:     # player input loop
        print("\nEnter your move => (r)ock (p)aper (s)cissors or (q)uit:")
        playMove = input()

        if playMove == 'q' or playMove == 'Q':
            print("\n")
            print("#########################################")
            print('Game Summary: %s Wins, %s Losses, %s Ties' % (wins, losses, ties))
            print("#########################################\n")
            
            # logic to decide outcome based on the game summary
            if wins > losses and wins > ties:
                print("You Won the game!")
            elif losses > wins and losses > ties:
                print("You lose the game!")
            elif ties > wins or ties > losses:
                print("It's a tie!")
            sys.exit()      # quits the program

        if playMove == 'r' or playMove == 'p' or playMove == 's':
            break
        print("Type one of r, p, s or q")


# display what the player chose

    if playMove == 'r':
        print("ROCK verse....")

    elif playMove == 'p':
        print("PAPER versus....")

    elif playMove == 's':
        print("SCISSORS versus....")


# display what the computer chose

    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")

    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")

    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")


# display records and count scores

    if playMove == computerMove:
        print("It's a tie!")
        ties += 1

    elif playMove == 'r' and computerMove == 's':
        print("You win!")
        wins += 1

    elif playMove == 's' and computerMove == 'p':
        print("You win!")
        wins += 1

    elif playMove == 'p' and computerMove == 'r':
        print("You win!")
        wins += 1

    elif playMove == 'r' and computerMove == 'p':
        print("You lose!")
        losses += 1

    elif playMove == 's' and computerMove == 'r':
        print("You lose!")
        losses += 1

    elif playMove == 'p' and computerMove == 's':
        print("You lose!")
        losses += 1


