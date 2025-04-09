# Mass Energy Equivalence

# This program calculates the energy equivalent of a given mass using the formula E = mc^2.
# The speed of light (c) is a constant: 299,792,458 m/s

c : int = 299792458  # Speed of light in m/s

def main() :
    # Get mass from user
    mass: float = float(input("\033[1;3m Enter mass in kilograms: "))
    # Calculate energy using E = mc^2
    energy: float = mass * c**2

    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("c = " + str(c) + " m/s")
    
    print(str(energy) + " joules of energy!")

if __name__ == "__main__":
    main()