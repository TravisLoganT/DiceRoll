import random

DICE_MIN = 1
DICE_MAX = 6


def get_random():
    return random.randint(DICE_MIN, DICE_MAX)


def roll_dice():
    print(f"\nRolling Dice:\nYou have rolled a {get_random()}\n")
    check_playing()


def check_playing():
    while True:
        print("Do you want to roll again?")
        continue_playing = input()
        if continue_playing == "yes" or continue_playing == "y":
            roll_dice()
        elif continue_playing == "no":
            exit()
        else:
            print("You have not inputted a valid input\n")


if __name__ == '__main__':
    roll_dice()


