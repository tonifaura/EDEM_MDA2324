import random

def game():
    # game choices
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    # game rules
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    # player's choice
    player = input("Enter your choice (rock, paper, scissors, lizard, spock): ")
    if player not in choices:
        print("Invalid choice. Please try again.")
        return game()

    # computer's choice
    computer = random.choice(choices)
    print("Computer chose: " + computer)

    # determine the winner
    if player == computer:
        print("It's a tie!")
    elif computer in rules[player]:
        print("You win!")
    else:
        print("You lose!")

game()