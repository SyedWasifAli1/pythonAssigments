def main():
    print("This program adds two numbers.")  # User ko bata rahe hain kya hone wala hai

    num1 : str = input("Enter first number: ")  # Pehla input liya (input default string hoti hai)
    num1 : int = int(num1)  # Us string ko integer me convert kiya

    num2 : str = input("Enter second number: ")  # Dusra input liya
    num2 : int = int(num2)  # Us string ko bhi integer me convert kiya

    total : int = num1 + num2  # Dono numbers ka sum nikala

    print("The total is " + str(total) + ".")  # Result print kiya with message


# Ye line ensure karti hai ke jab ye file run ho to `main()` function execute ho.
if __name__ == '__main__':
    main()
