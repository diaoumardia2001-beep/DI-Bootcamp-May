# Mini-project: Rock, Paper, Scissors
# Rock-paper-scissors is an old game that can be played between two people. You can read about it in wikipedia

# We will create a game for the user to play Rock-paper-scissors against the computer.

# The user will input his/her move (rock/paper/scissors),
# and the computer will select either rock, paper or scissors at random.
# We will then compare the user’s move with the computer’s move, and determine the results of the game:

# The user won

# The computer won (the user lost)
# A draw (tie)
# We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.

# The user will be able to play again and again. Once the user decides to exit the program, we will print a summary of the outcomes of all the games: how many times they won, lost or and tied the computer.

# Here’s some example output:


# Steps
# Part I - game.py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

import random

class Game:
    def get_user_item(self):
        valid_items = ["rock", "paper", "scissors"]
        while True:
            user_input = input("Choose rock, paper or scissors: ").strip().lower()
            if user_input in valid_items:
                return user_input
            print("Invalid choice. Please choose rock, paper or scissors.")
    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        winning_combinations = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }
        if winning_combinations[user_item] == computer_item:
            return "win"
        return "loss"
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou selected {user_item}. The computer selected {computer_item}.", end=" ")
        if result == "win":
            print("You win! 🏆")
        elif result == "draw":
            print("You drew! 🎲")
        else:
            print("You lose! 😭")

        return result