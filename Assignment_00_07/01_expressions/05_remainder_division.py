# Remainder and Division
# The remainder of a division operation can be obtained using the modulus operator (%).
# The integer division can be performed using the double division operator (//).

def main():
    #  Get user input for two numbers
    dividend:int = int(input("\033[1;3m Enter the number to be divided: "))
    divisor: int = int(input("\033[1;3m Enter the number to divide by: "))
    # Calculate the remainder and integer division

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor
    # Display the results
    print(f"The result of the division is: {quotient} with a remainder of {remainder}.")

if __name__ == "__main__":
    main()