def main():
    # Step 1: User se input lena
    num = float(input("Type a number to see its square: "))
    
    # Step 2: Calculate square of the number
    square = num ** 2  # num * num is equivalent to num ** 2
    
    # Step 3: Print the result
    print(f"{num} squared is {square}")


# Required line to call the main() function
if __name__ == '__main__':
    main()
