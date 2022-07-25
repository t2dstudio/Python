# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#            temperatures.append(int((row[1])))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))  # The object type of the entire csv is a dataframe
#print(type(data["temp"])) # The list of data in the file is refered to as Series in PANDAS

# data_dict = data.to_dict()
# print(data_dict)
temp_list = data['temp'].to_list()
#print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

#USING PANDAS SERIES CLASS TO CALCULATE AVERAGE "mean"
#data['temp] is same as data.temp in Pandas
# avg = data["temp"].mean()
# largest = data['temp'].max()
# print(largest)

#GET DATA IN ROWS
#print(data[data['day'] =="Monday"])

#WHICH ROW HAS THE HIGHEST TEMP IN A WEEK
print(temp_list)
#print(data[data['temp'] == largest])
# monday =data[data['temp'] == largest]
# print(monday.condition)

#create dataframe from scract

my_data = {
    "students": ["Kenny", "Tee", "Amy"],
    "scores": [77,78,90]
}
#To convert the dict to a dataframe
your_data = pandas.DataFrame(my_data)
your_data.to_csv("new_data.csv")
