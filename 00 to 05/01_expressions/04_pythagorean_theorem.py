import math  # Import math module to use sqrt()

def main():
    # Step 1: User input for two perpendicular sides
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Step 2: Apply Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)

    # Step 3: Output the hypotenuse
    print("The length of BC (the hypotenuse) is: " + str(bc))

# Standard main function call
if __name__ == '__main__':
    main()
