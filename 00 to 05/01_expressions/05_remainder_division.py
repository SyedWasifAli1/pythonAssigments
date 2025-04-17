def main():
    # Step 1: User input
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Step 2: Do integer division and get remainder
    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    # Step 3: Output result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
