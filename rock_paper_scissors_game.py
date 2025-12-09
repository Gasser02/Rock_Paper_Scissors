

""" Rock Paper Scissors game """

import random

# Constants 
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

EMOJIS = {
    ROCK: "👊🏼",
    PAPER: "📃",
    SCISSORS: "✂️"
}

CHOICES = tuple(EMOJIS.keys())


def get_user_choice():
    """Ask the user to input r/p/s and return the valid choice."""
    while True:
        user_choice = input("Rock, Paper, or Scissors (r/p/s): ").lower().strip()
        if user_choice in CHOICES:
            return user_choice
        print("Invalid choice, try again.")


def display_choices(user_choice, comp_choice):
    """Print the emoji versions of user and computer choices."""
    print(f"You chose: {EMOJIS[user_choice]}")
    print(f"Computer chose: {EMOJIS[comp_choice]}")


def determine_winner(user_choice, comp_choice):
    """Determine and print the result of the game."""
    if user_choice == comp_choice:
        print("Tie!")
        return
    
    if (
        (user_choice == ROCK and comp_choice == SCISSORS)
        or (user_choice == PAPER and comp_choice == ROCK)
        or (user_choice == SCISSORS and comp_choice == PAPER)
    ):
        print("You WON!")
    else:
        print("You LOST!")


def play_game():
    """Main game loop."""
    while True:
        user_choice = get_user_choice()
        comp_choice = random.choice(CHOICES)

        display_choices(user_choice, comp_choice)
        determine_winner(user_choice, comp_choice)

        ask = input("Wanna continue? (y/n): ").lower().strip()
        if ask == "n":
            break


play_game()






