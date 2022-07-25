
import random
"""
LOOPS
for item in list
"""
"""
Average Height exercise

student_heights = input("Input a list of student heights ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# result = sum(student_heights)/ len(student_heights)
# print(round(result))
total_height = 0
for height in student_heights:
  total_height += height
print(total_height)
number_of_student = 0
for student in student_heights:
  number_of_student += 1
print(number_of_student)
average_height = round(total_height / number_of_student)
print(average_height)
"""
"""
For loop in a list
High Score exercise
without using min() or max()

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score =0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest_score is : {highest_score}")
"""
"""
FOR LOOP WITH RANGE
for number in range(a, b)
  do something
"""
"""
EXERCISE (multiple all the even number in 1- 100)

sum_of_even_numbers = 0
for number in range(2, 101, 2): # step size is 2
  # print(number)
  sum_of_even_numbers += number
print(sum_of_even_numbers)
"""
"""
FIZZBUZZ EXERCISE

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
      print(f"{number}  = FizzBuzz")
    elif number % 3 == 0:
      print(f"{number}  = Fizz")
    elif number % 5 == 0:
      print(f"{number} Buzz")
    else:
      print(f"{number} = {number}")
"""
"""
PASSWORD GENERATOR EXERCISE
"""


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""EASY LEVEL GENERATING RANDOM FOR EASH CATEGORY"""
# password = ""
# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)
#
# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)
#
# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)
#
# print(password)

"""HARD LEVEL GENERATING RANDOM IN A NON-SEQUENTIAL ORDER"""

password_list = []
for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char
print(f" Your password is {password}")
