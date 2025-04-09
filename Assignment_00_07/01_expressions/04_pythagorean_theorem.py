# Pythagorean theorem
# The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.

import math

def main():
    # Get the lengths of two sides from the user

    ab:float = float(input("\033[1;3m Enter the length of a side AB: "))
    ac:float = float(input("\033[1;3m Enter the length of a side AC: "))

    bc:float= math.sqrt(ab**2 + ac**2)
    # Print the length of the hypotenuse
    print(f"The length of the hypotenuse BC is: {bc:.2f}")

if __name__ == "__main__":
    main()