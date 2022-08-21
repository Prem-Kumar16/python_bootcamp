# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

for_t = name1_lower.count("t") + name2_lower.count("t")
for_r = name1_lower.count("r") + name2_lower.count("r")
for_u = name1_lower.count("u") + name2_lower.count("u")
for_e = name1_lower.count("e") + name2_lower.count("e")

for_true = for_t + for_r + for_u + for_e

for_l = name1_lower.count("l") + name2_lower.count("l")
for_o = name1_lower.count("o") + name2_lower.count("o")
for_v = name1_lower.count("v") + name2_lower.count("v")

for_love = for_l + for_o + for_v + for_e

total_score = (for_true * 10) + for_love

if total_score < 10 or total_score > 90 :
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50 :
    print(f"Your score is {total_score}, you are alright together.")
else :
    print(f"Your score is {total_score}.")
