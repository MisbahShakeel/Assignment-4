import random

num_Sides = 6

def roll_dice() :
    """ Smimulate rolling a two dice and print their total """

    die1 = random.randint(1, num_Sides)
    die2 = random.randint(1, num_Sides)
    total = die1 + die2
    print("The total of the two dice is", total)

def main() :
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

if __name__ == "__main__" :
    main()