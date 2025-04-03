# -------- Square Number --------
# This script defines a function that takes a number as input and returns its square.

def main():
    number = float(input("Enter a number to square: "))
    print(str(number) + " squared is " + str(number ** 2))

if __name__ == "__main__":
    main()