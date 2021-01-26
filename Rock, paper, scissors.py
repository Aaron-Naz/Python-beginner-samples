# Rock, paper, scissors game
from random import randint

# moves for the player
moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0, 2)]  # computer move assigned as random element from "moves" list
    player = input("Type rock, paper, scissors or end game ").lower()
    if player == "end game":
        print("Game over!")
        break
    elif player == computer:
        print("Tie :|")
    elif player == "rock":
        if computer == "paper":
            print(f"Computer chose {computer}, you lost! :(")
        else:
            print(f"Computer chose {computer}, you win! :)")
    elif player == "paper":
        if computer == "scissors":
            print(f"Computer chose {computer}, you lost! :(")
        else:
            print(f"Computer chose {computer}, you win! :)")
    elif player == "scissors":
        if computer == "rock":
            print(f"Computer chose {computer}, you lost! :(")
        else:
            print(f"Computer chose {computer}, you win! :)")
    else:
        print("Please choose from the given options only.")
