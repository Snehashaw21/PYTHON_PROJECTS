#Creating snake,water and gun game:

import random

# Choice Type
choices = ['snake', 'water', 'gun']

# Computer randomly select
computer = random.choice(choices)

# User input/choice
user = input("Enter your choice: ").lower()

# Print computer's choice
print("Computer chose:", computer)

if computer == user:
    print("It's a tie!")
elif computer == 'snake' and user == 'water':
    print("Computer wins!")
elif computer == 'water' and user == 'gun':
    print("Computer wins!")
elif computer == 'gun' and user == 'snake':
    print("Computer wins!")
else:
    print("You win!")
