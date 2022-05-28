from random import randint

"""
Simple Guess the Number game, where user has to guess a computer's randomly generated number from 1 to n.
"""

LIVES = 0


def choose_difficulty():

    """
    Certain letter choosing a difficulty, which is connected to number of LIVES
    """

    global LIVES

    while True:

        difficulty = input("""
        Choose your difficulty.
        Easy (10 Lives) - press 'e'
        Normal (5 Lives) - press 'n'
        Hard  (3 Lives) - press 'h'
        --------------------------
        """).lower()

        if difficulty not in "enh":
            print("Please choose your difficulty by typing one of the letters:'e','n','h'\n")
        elif difficulty == 'h':
            LIVES = 3
            print(f"Difficulty: HARD. You have {LIVES} lives. Good luck!\n")
            break
        elif difficulty == 'n':
            LIVES = 5
            print(f"Difficulty: NORMAL. You have {LIVES} lives. Good luck!\n")
            break
        elif difficulty == 'e':
            LIVES = 10
            print(f"Difficulty: EASY. You have {LIVES} lives. Good luck!\n")
            break


def computer_range_number():

    """
    Setting an ending range number for computer
    :return: Ending range number
    """

    while True:

        try:
            computer_range = int(input("Write a number between 1 to n to create a range for computer.\n"
                                       "The higher the number the harder to guess: "))
        except ValueError:
            print(f"Please choose a number\n")

        else:
            print(f"Computer range is between 1 and {computer_range}\n")
            break

    return computer_range


def computer_random_number(number):
    f"""
    :param: number that was chosen in function computer_range_number". 
    :return: random number between 1 and 'computer_range_number'
    """

    computer_random = randint(1, number)

    return computer_random

# Game Starts Here

is_game_on = False

while not is_game_on:

    choose_difficulty()
    range_comp = computer_range_number()
    computer_number = computer_random_number(range_comp)

    while LIVES > 0:

        try:

            guess = int(input(f"You have {LIVES} lives.\nTry to guess a computer number between 1 and {range_comp}: "))

        except ValueError:

            print("Wrong value\n")
            continue

        else:
            if guess == computer_number:
                print(f"Correct! You guessed computer number: {computer_number}\n")
                break
            elif guess > computer_number:
                print("Too high\n")
                LIVES -= 1
            else:
                print("Too low\n")
                LIVES -= 1

        if LIVES == 0:
            print("Sorry. You have lost!\n")

    while True:
        g = input("Do you want to play again? y/n\n").lower()

        if g not in "yn":
            print("Choose 'n' or 'y'.")
            continue
        elif g == "y":
            break
        elif g == "n":
            print("Thanks for playing")
            is_game_on = True
            break



