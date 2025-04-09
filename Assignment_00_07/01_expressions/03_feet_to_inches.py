# Convert feets in to inches
# 1 feet = 12 inches

inches_per_feet: int = 12

def main() :
    feet:float = float(input("Enter feets: "))
    inches:float = feet * inches_per_feet
    print("That is ", inches, " inches")

if __name__ == "__main__":
    main()