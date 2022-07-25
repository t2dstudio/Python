# print(len(input("What is your name?\n")))
# name = input("What is your name?\n")
# print("Your name is " + name)

# a = input("a:")
# b = input("b: ")
#
# c = a
# a = b
# b = c





# print("a = " + a)
# print("b = " + b)

# print(round(8/3, 2))  # two decimal places
# print(8//3)

# score =0,
# height = 1.8
# is_winning = True
# print(f"Your score is {score} and height {height} is {is_winning}")


# age = input("what is your current age?\n")
# year = int(age) * 365
# month = year//12
# day = month//30
#
# print(f"You have {year} years, {month} months, {day} days to finish")

# Conditional Operations
#If else
# if condition:
# print("welcome to the rollercoaster")
# height = int(input("What is your height in cm?"))
# if height >= 120:
#     print("You can ride")
# else:
#     print("Sorry, you cant ride")

# my_number = int(input("Enter Your Number\n"))
# is_even = int(my_number / 2)
#
# if my_number % 2 == 0:
#     print(f"{my_number} is even because {my_number}% 2 = {is_even}")
# else:
#     print(f"{my_number} is not even because {my_number}% 2 = {is_even}")

# Nested If
# height = float(input("Enter your height\n"))
# weight = float(input("Enter your weight\n"))
# bmi = round(weight/height ** 2)
# if bmi < 18.5:
#     print("underweight")
# elif bmi < 25:
#     print("normal weight")
# elif bmi < 30:
#     print("overweight")
# elif bmi < 35:
#     print("Obese")
# else:
#     print("clinicallu obese")

"""Leap Year Challenge
on every year that is evenly divisible by 4
except every year that is evenly divisible by 100
unless the year is also evenly divisible by 400

year = int(input(" Enter the year\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("is leap year")
        else:
            print("is not leap")
    else:
        print("is leap year")
else:
    print("is not leap year")"""
""""Multiple if
Pizza Order Exercise
Small pizza: $ 15
Medium Pizza: $ 20
Large Pizza: $ 25

Pepperoni for small Pizza: +$2
Pepperoni for Medium or Large: +$3

Extra cheese for any size pizza: +$1
"""
"""print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input(" Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill for {size} size of Pizza is {bill}")
    print(f"Your bill for {size} size of Pizza is {bill}")

elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill for {size} size of Pizza is {bill}")
    print(f"Your bill for {size} size of Pizza is {bill}")

if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill for {size} size of Pizza is {bill}")
    print(f"Your bill for {size} size of Pizza is {bill}")

else:
    print("Please enter a valid size")"""

"""LOGICAL OPERATORS (AND. OR, NOT)
love calculator

print("Welcome to Python Love Calculator")
name1 = input("What is your name \n")
name2 = input(" What is their name\n")

name1_to_lowercase = name1.lower()
name2_to_lowercase = name2.lower()

combine_name = name1_to_lowercase + name2_to_lowercase

t_check = combine_name.count('t')
r_check = combine_name.count('r')
u_check = combine_name.count('u')
e_check = combine_name.count('e')
l_check = combine_name.count('l')
o_check = combine_name.count('o')
v_check = combine_name.count('v')
e2_check = combine_name.count('e')
true = t_check + r_check + u_check + e_check
love = l_check + o_check + v_check + e2_check

general_score = str(true) + str(love)
love_score = int(general_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
"""
"""TREASURE ISLAND PROJECT
"""
print("Welcome to Treasure island\n Your mission is to find the treasure")
stage1 = input("Do you want to go Left or Right\n")
if stage1 == "R":
    print("Game Over")
elif stage1 == "L":
    stage2 = input("Do you want to Swim or Wait\n")
    if stage2 == "S":
        print("Game Over")
    elif stage2 == "W":
        stage3 = input("Which door? Red, Blue, Yellow\n")
        if stage3 == "B" or "R":
            print("Game Over")
        elif stage3 == "Y":
            print("You win")


