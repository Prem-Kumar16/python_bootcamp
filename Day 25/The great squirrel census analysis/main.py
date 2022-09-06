# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # total_temp = 0
# # for temp in temp_list:
# #     total_temp += temp
# #
# # avg_temp = round(total_temp / len(temp_list))
# avg_temp = data["temp"].mean()
# print(f"The average temp is {avg_temp}")
#
# max_temp = data["temp"].max()
# print(max_temp)

# Getting row values

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * (9/5) + 32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_sq = len(data[data["Primary Fur Color"] == "Gray"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_sq, black_sq, cinnamon_sq)

data_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_sq, black_sq, cinnamon_sq]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("sq_fur_color.csv")
