student_dict = {
    "students": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}
#Looping through a dictionary
# for (key,value) in student_dict.items():
#     print(value)

import pandas
pd = pandas.DataFrame(student_dict)
print(pd)

#Looping Through a Dataframe
# for (key,value) in pd.items():
#     print(value)

#Pandas loop method for rows instead of columns (iterrow)
for (index, row) in pd.iterrows():
    #print(row.students)
    if row.score > 80:
        print(row.students)





# TODO : You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in
#  the given sentence and calculates the number of letters in each word.
#
# Try Googling to find out how to convert a sentence into a list of words.
#
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

# Example Output
# 'What': 4,
# 'is': 2,
# 'the': 3,
# 'Airspeed': 8,
# 'Velocity': 8,
# 'of': 2,
# 'an': 2,
# 'Unladen': 7,
# 'Swallow?': 8
# }