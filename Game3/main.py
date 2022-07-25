import random
from game_data import data
from art import logo, vs
from replit import clear
"""# Randomly loop through dataList and provide two details

user_rating = 0
actual_rating = 0
def generate_random_celebrity():
    #print(random.choice(data))
    return(random.choice(data))





# ask user to input data with highest ratings
def user_answer():
    user_input = input("Who has more rating? Type A or B: \n")
    return user_input




# Check actual result against user input
# If user is right check answer against another random data until the user result is false

print(logo)

computer_output1 = generate_random_celebrity()
name1 = computer_output1['name']
rating1 = computer_output1['follower_count']
description1 = computer_output1['description']
country1 = computer_output1['country']
print(f"Compare A: {name1}, a {description1}, from {country1} and rating = {rating1}")

print(vs)

computer_output2 = generate_random_celebrity()
name2 = computer_output2['name']
rating2 = computer_output2['follower_count']
description2 = computer_output2['description']
country2 = computer_output2['country']
print(f"Compare B: {name2}, a {description2}, from {country2} and rating = {rating2}")


def user_selection():
    if user_answer() == 'A':
        return rating1
    if user_answer() == 'B':
        return rating2

def highest_rating():
    highest = max(rating1, rating2)
    return highest

#Compare two data
def compare_two_celebrity(user_rating, actual_rating):
    print(f"user rating = {user_rating}")
    print(f"actual rating = {actual_rating}")
    if user_rating == actual_rating:
        print("you win")
    else:
        print("You lose")


compare_two_celebrity(user_selection(), highest_rating())

"""



def format_data(account):
    """ #3.Format the data into a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    # 5bUse If statement to check if user is correct
    if a_followers > b_followers:
        return guess == "a" # This will return true if guess == a
    else:
        return guess == "b"


#1. Display Art
print(logo)
score = 0
game_should_continue = True
# 2. Generate a random account from the game data
account_b = random.choice(data)

#8. Make the gane repeatable
while game_should_continue:

    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #4. Ask for a guess
    guess = input("Who has more followers? Type A or B: \n").lower()
    #5. Check if user is correct
    #5a Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    clear()
    print(logo)

    #6. Give a feedback of the guess
    #7Score Keeping
    if is_correct:
        score += 1
        print(f"You are right. Current Score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry you are wrong. Final Score: {score}")




