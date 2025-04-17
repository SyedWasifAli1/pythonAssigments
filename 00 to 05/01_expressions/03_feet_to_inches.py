"""
An example program with constants
This program converts feet to inches.
"""

# Constant: Number of inches in 1 foot
INCHES_IN_FOOT: int = 12

def main():
    # Step 1: Ask user for number of feet
    feet: float = float(input("Enter number of feet: "))

    # Step 2: Convert to inches
    inches: float = feet * INCHES_IN_FOOT

    # Step 3: Show result
    print("That is", inches, "inches!")

# Required boilerplate to run main
if __name__ == '__main__':
    main()
