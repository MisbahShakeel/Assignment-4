# -------- Temperature Converts Fahrenheit to Celsius --------
# This program converts Fahrenheit to Celsius

def main():
    print("Welcome to the Ferhenheit to Celsius converter program!")

    # Get the temperature in Fahrenheit from the user
    try:
        farhenheit = float(input("\033[1;3m Enter the temperature in Ferhenheit: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Convert the temperature to Celsius
    celsius = (farhenheit - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius:.2f}°C")

if __name__ == "__main__":
    main()