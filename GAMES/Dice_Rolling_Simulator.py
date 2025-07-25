#Dice Rolling Simulator game:


import random

print(" Welcome to the Dice Rolling Simulator!")

while True:
    input("Press Enter to roll the dice..")
    
    # Roll the dice
    dice = random.randint(1, 6)
    
    print(f"\nYou rolled a {dice}!")

    # Ask user if they want to roll again
    again = input("Do you want to roll again? (yes/no): ")
    if again.lower() != 'yes':
        print("Thanks for playing.")
        break
