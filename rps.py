# Rock paper scissors game against a random computer
# Choose "r", "s" or "p" to play

import random


def play():
    # Getting the user input
    user = input("Type 'r' for rock, 'p' for paper, 's': ").lower()
    # Computer generates a random selection
    computer = random.choice(["r", "p", "s"])

    # If selections are equal this match is a tie
    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won"

    return "You lost"


# Choosing a winner
def is_win(player, robot):
    if (player == "r" and robot == "s") or (player == "s" and robot == "p") or (player == "p" and robot == "r"):
        return True


print(play())
