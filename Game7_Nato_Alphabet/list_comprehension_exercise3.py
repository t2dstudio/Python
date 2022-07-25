with open("file1.txt", "r") as file1:
    new_file1 =file1.readlines()
    f1_list = [int(number) for number in new_file1]
f2 = open("file2.txt")
new_file = f2.readlines()
f2_list = [int(num) for num in new_file]

result = [number for number in f1_list if number in f2_list ]

print(result)