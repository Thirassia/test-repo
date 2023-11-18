"""Module providing a function for checking leap years."""


def is_leap_year(year):
    """
    Check if the year is divisible by 4 and either 
    not divisible by 100 or divisible by 400
    """

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Test the function
year_to_check = int(input("Enter a year: "))

if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")

else:
    print(f"{year_to_check} is not a leap year.")
