# Random dice roll simulation

import random

num_Sides:int = 6

def main() :
    dice1: int = random.randint(1, num_Sides)
    dice2:int = random.randint(1, num_Sides)

    total:int = dice1 + dice2

    print(f"Dice have: {num_Sides} sides each.")
    print(f"First dice: {dice1}")
    print(f"Second dice: {dice2}")
    print(f"Total of two dice: {total}")

if __name__ == "__main__":
    main()