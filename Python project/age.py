
try:
    age_str =int(input("ENTER THE AGE IS "))
    if age_str >= 18:
        print("You are eligible for voting.")
    elif age_str < 0:
        print("Age cannot be a negative number.")
    else:
        print("You are not eligible for voting.")

except ValueError:
    print("That's not a valid whole number! Please run the program again.")
    # this comments tags used this variables to be used to
    """""
    this used to more comment in python are usingf this progeam lite
    """
    
