SENTENCE_START: str = "Python is fun. I learned to program and used Python to make my "  # Sentence template

def main():
    # User se input lete hain (adjective, noun, verb)
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # Sentence ko print karte hain jo user ke input se complete ho gaya hai
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

# Code ko execute karne ka logic
if __name__ == '__main__':
    main()
