# -------- Triangle Perimeter --------
# Take the lengths of the three sides of a triangle from user, this program calculates the perimeter of the triangle.

def main():
    side1 = float(input("\033[1;3m Enter the lenght of side 1 : "))
    side2 = float(input("\033[1;3m Enter the lenght of side 2 : "))
    side3 = float(input("\033[1;3m Enter the lenght of side 3 : "))

    # print the perimeter of the triangle
    print("The perimeter of the triangle is : " + str(side1 + side2 + side3))

if __name__ == "__main__":
    main()