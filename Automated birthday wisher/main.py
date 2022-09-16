import datetime as dt
import smtplib
import random
import pandas

letter_template = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

my_email = "premrajreddy26@gmail.com"
password = "mjtrnbiprsgkejxs"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")
birthday_list = birthday_data.to_dict(orient='records')

now = dt.datetime.now()
present_day = now.day
present_month = now.month

for member in birthday_list:
    if present_day == member["day"]:

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv

        random_letter = random.choice(letter_template)

        with open(f"letter_templates/{random_letter}", "r") as letter:
            data = letter.read()
            data = data.replace("[NAME]", member["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=member["email"], msg=f"Subject:Happy birthday!!!\n\n"
                                                                                  f"{data}")
