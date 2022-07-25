######  SCOPES ########
# Local Scopes
# Variable, function etc that exists within a function
#Global Scope
#Available anywhere eg within and outside functions

# There is no block scope in Python unlike java
# Variables within an if,while,for and anything that has a : is not considered as a seperate variable
"""
game_level = 3
if game_level < 5:
    new_game_level = 15
print(new_game_level)
Note Here that i can access new_game_level outside the if statement
"""
"""
#Modifying the Global Scope
enemies = 1
def increase_enemies():
    #global enemies # This is modifying the enemies at the global level DONT DO INTEAD use return
    #enemies += 2
    print(f" enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f" enemies outside function: {enemies}")

"""
###### GLOBAL CONSTANTS ##########
# Usually denoted by ALL CAPS. This reminds you not to change he value whe used in your code
PI = 3.14159
URL ="https://www.google.com"
TWITTER_HANDLE = "@khandle"


