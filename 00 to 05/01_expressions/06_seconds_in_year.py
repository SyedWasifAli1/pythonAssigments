# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365         # Number of days in a year
HOURS_PER_DAY: int = 24          # Number of hours in a day
MIN_PER_HOUR: int = 60           # Number of minutes in an hour
SEC_PER_MIN: int = 60            # Number of seconds in a minute

def main():
    # Calculate the number of seconds in a year
    total_seconds: int =  DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print the result nicely
    print("There are " + str(total_seconds) + " seconds in a year!")


# This provided line is required to call the main() function
if __name__ == '__main__':
    main()
