from random import randint
from number_guessing_logo import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


#Choose a random number from 1-100
answer = randint(1, 100)
# Function to check guess vs actual
def check_answer(guess, answer, turns):
    """Check answers against guess. Returns the no of turns remaining"""
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
       print(f" You got it! The answer was {answer}.")

# Make a function to call difficulty
def set_difficulty():
    level = input("Choose a difficulty 'Easy' or 'Hard' \n")
    if level =="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print(logo)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f" You have {turns} attempts remaining to guess the number")
   #Let the user guess a number
        print(answer)
        guess = int(input("Make a guess:\n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You run out of guess. you lose")
            return
        elif guess != answer:
            print("Guess again.")
    # Track and reduce number of guess by 1

game()











#
# easy = [1,2,3,4,5]
# hard = [1,2,3,4,5,6,7,8,9,10]
# attempts = len(easy)
# game_over = False
# output = input("Choose a difficulty. Type 'easy' or 'hard'\n")
# while attempts > 0:
#     if output == "easy":
#         guessed_number = int(input("Make a guess\n"))
#         if guessed_number in easy:
#             print("You won")
#             game_over=True
#         else:
#             attempts += -1
#             print(f"You have {attempts} attempts remaining to guess the number")
#     if output == "hard":
#         hard_attempts = len(hard)
#         guessed_number = int(input("Make a guess\n"))
#         if guessed_number in hard:
#             print("You won")
#             game_over = True
#         else:
#             hard_attempts += -1
#             print(f"You have {hard_attempts} attempts remaining to guess the number")
#
# print("You lose")