#File Not Found
# with open("No_file.txt", "r") as file:
#     file.read()
#Key Error
# a_dictionary = {"Key": "value"}
# print(a_dictionary["non_existing_key"])
#Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# print(fruit_list[3])
#TypeError
# text = "abc"
# print(text + 5)

#.............CATCHING EXCEPTION...........................# Try....Except....else....Finally
#.........TRY = Something that might cause an exception
#.........EXCEPT = Do this if there was an exception
#.........ELSE = Do this if there were no error
#.........FInally = Do this no matter what happens
#File Not Found
"""
try:
    file = open("No_file.txt")
    a_dictionary = {"Key": "value"}
    print(a_dictionary["non_existing_key"])
except FileNotFoundError:
    open("No_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The Key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
"""

#.........................RAISING YOUR OWN EXCEPTION
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be more than 3 meters.")
bmi = weight / height **2
print(bmi)

# Check Use Case in Game7_Nato Game Main.py




