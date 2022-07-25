"""DICTIONARIES & NESTING
allows to group and tie related value to a key like a folder
empty_dict = {}
# Adding
empty_dict["sport"] = "Soccer"
#Edit
empty_dict["sport"] = "Football"

#Looping through Dict
for key in empty_dict
    print(key)
    print empty_dict[key]
"""

"""Exercise One
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {
    91-100: "Outstanding",
    81-90: "Exceed Expectation",
    71-80: "Acceptable",
    0-70: "Fail"
}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceed Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
"""
"""NESTING
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dict
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg","Stutgart"],
}
# Nesting a dict in a dict
travel_log = {
    "France": {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited" : ["Berlin", "Hamburg","Stutgart"],"total_visits": 50},
}

# Nesting a dict inside a list (Remember list are indexed meaning you can only access using position(0,1,2)but dict are accessed using their key)
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {"country": "Germany",
     "cities_visited" : ["Berlin", "Hamburg","Stuttgart"],
     "total_visits": 50
     },
]
"""
"""EXERCISE"""
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇
def add_new_country(country_visited,times_visited,cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)