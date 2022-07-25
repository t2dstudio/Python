weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

weather_f = {weekday:(temp_c * 9/5) + 32 for (weekday, temp_c) in weather_c.items()}
# Write your code 👇 below:

print(weather_f)



# TODO : You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes
#  each temperature in degrees Celsius and converts it into degrees Fahrenheit.
#
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.w to convert a sentence into a list of words.
#
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

# Example Output
# 'Monday': 53.6,
# 'Tuesday': 57.2,
# 'Wednesday': 59.0,
# 'Thursday': 57.2
# 'Friday': 69.8,
# 'Saturday': 71.6,
# 'Sunday': 75.2
# }