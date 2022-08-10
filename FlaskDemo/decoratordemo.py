import time

#.....A Decorator function is a function that wraps another function and gives ir some additional fnctionality or modifies the functionality
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #Do something before
        function()
        #Do something after

    return wrapper_function

#@delay_decorator
def say_hello():
    print("Hello")
@delay_decorator
def say_bye():
    print("Byeeee")

def say_greeting():
    print("How are You")

say_hello()
say_bye()
# say_greeting()