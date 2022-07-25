'''
Function (Normal)
def my_function():
  Do something

Function with Inputs
def my_function(something):
  Do this with something
  Then do this

'''
# Functions with Outputs

'''
def my_function():
    result = 3 * 2
    return result
'''

'''
# Write a function to convert to Title case
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Fields should not be empty"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f'{formatted_f_name} {formatted_l_name}'


print(format_name(input("what id your first name? "), input("what"
                                                            "is your last name ")))
'''
# Leap Year re-factor using RETURN keyword
'''
Instructions
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

Hint
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

Be careful with indentation.
'''
'''

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
'''

# DOCSTRINGS - Declared immediately after a funct is defined
def format_my_name(f_name, l_name):
    """Take a firsname and lastmname and do something
    """
    return f_name

format_my_name()