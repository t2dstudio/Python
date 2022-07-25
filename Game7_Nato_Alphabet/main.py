#....................LIST COMPREHENSION......................................

# numbers = [1,2,4,5,7,8]
# new_list = [n+1 for n in numbers]
# print(new_list)
#
# name = "Kehinde"
# new_letter = [letter for letter in name]
# print(new_letter)

#.........................CONDITIONAL LIST COMPREHENSION.............................
#.............new_list=[new_item for item in list if test]...........................
# names = ["Kenny", "Bola", "Mope"," Blessing", "Richard"]
# new_name =[name for name in names if len(name)< 5]
# upper_case_name = [name.upper() for name in names if len(name) > 5]
# print(upper_case_name)

#.................DICTIONARY COMPREHENSION..........................................
#.....Helps us to create a new dictionary from a list of another dictionary............
#...........new_dict = {new_key:new_value for item in list...............}
#...........new_dict = {new_key:new_value for (key, value) in dict.items()}...............
#...........new_dict = {new_key:new_value for (key, value) in dict.items() if test}...............
# import random
# names = ["Kenny", "Bola", "Mope"," Blessing", "Richard"]
# student_scores = {student: random.randint(1, 100) for student in names}
# #print(new_dict)
# passed_students = {student:score for (student,score) in student_scores.items() if score >= 60 }
# print(passed_students)
import pandas
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_dict = {row.letter:row.code for (index,row) in nato_data.iterrows()}
# print(nato_data_dict.keys)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word").upper()
    try:
        nato_list = [nato_data_dict[letter] for letter in word]
    except KeyError:
        print("Sorry Only letters in the alphabets please")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()


