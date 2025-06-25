#STONE,PAPER AND SCISSORS GAMES:

import random

print("Welcome to Stone, Paper, Scissors Game!")

#user input
user = input("Your turn: ").lower()

# Computer choice
options = ['stone', 'paper', 'scissors']
computer = random.choice(options)

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == 'stone' and computer == 'scissors') or \
     (user == 'scissors' and computer == 'paper') or \
     (user == 'paper' and computer == 'stone'):
    print("You win!")
elif user in options:
    print("You lose!")
else:
    print("Invalid input. Please choose stone, paper, or scissors.")
