from turtle import Turtle, Screen


# ken = Turtle()
# print(ken)
# ken.shape("turtle")
# ken.color("coral")
# ken.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
# Attributes are the things that the object has
# Methods are the things that the object do
class User:
    def __init__(self,user_id, username): # Constructor
        self.id = user_id
        self.username = username
        self.follower = 0 # Setting a default value for the attribute
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user1 = User("001",  "Kenny")
user2 = User("002", "Tenny")
print(user1.id)

#ADDING METHODS TO CLASSES
