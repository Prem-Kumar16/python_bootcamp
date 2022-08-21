import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_members = len(names) - 1 #Coz lists starts from 0
#print(total_members)
who = random.randint(0,total_members)
#print(who)
print(f"{names[who]} is going to buy the meal today!")
