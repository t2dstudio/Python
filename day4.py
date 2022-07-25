""""
RANDOMISATION AND PYTHON LISTS
"""
import random

# random_integer = random.randint(1,10)
# print(random_integer)

# Random floating point
#0.0000000 - 0.999999999
# random_float = random.random() * 5
# print(random_float)
# random_integer = random.randint(1, 2)
# if random_integer == 1:
#     print("tail")
# else:
#     print("head")

"""
PYTHON LIST []
-data structure for storing data
fruits = [mango, guava]
.append
"""
"""
Exercise 1

name_string = input("Give me everybodys names, seperated by a comma\n")
names = name_string.split(", ")
# random_name = random.choices(names)
# print(f"{random_name} will pay for the bill ")

random_range = random.randint(0, (len(names) -1))
name_to_pay = names[random_range]
print(f"{name_to_pay}  will pay for the meal")
"""
"""
Exercise 2

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map1 = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n" )
horizontal = int(position[0])
vertical = int(position[1])

map1[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

"""
"""
EXERCISE 3 (ROCK PAPER SCISSORS)
"""
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
output = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock. 1 for Paper or 2 for Scissors\n"))
if user_input >= 3 or user_input < 0:
    print("You typed invalid number, you lose")
else:
    print(output[user_input])

    computer_response = random.randint(0, 2)
    print("Computer chose:")
    print(output[computer_response])

    if user_input == 0 and computer_response == 2:
        print("You wins")
    elif computer_response == 0 and user_input == 2:
        print("You lose")
    elif computer_response > user_input:
        print("You Lose")
    elif user_input > computer_response:
        print("You win")
    elif computer_response == user_input:
        print("Its a draw")

