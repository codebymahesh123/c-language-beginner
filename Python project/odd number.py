# Use a try-except block to make sure the user enters a valid number.
try:
    # 1. Get the number from the user
    # int() converts the input string into a whole number
    number_str = int(input("enterr number of number"))

    # 2. Check if the remainder (%) when divided by 2 is 0
    if (number_str % 2) == 0:
        # 3. If the remainder is 0, it's even
        print(f"The number {number_str} is EVEN.")
    else:
        # 4. If the remainder is not 0 (it's 1), it's odd
        print(f"The number {number_str} is ODD.")

except ValueError:
    # This runs if the user enters text (like "hello") instead of a number
    print("That's not a valid whole number! Please run the program again.")