# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_in_int = int(age)

remaining_yr = 90 - age_in_int

days = 365 * remaining_yr
weeks = 52 * remaining_yr
months = 12 * remaining_yr

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
