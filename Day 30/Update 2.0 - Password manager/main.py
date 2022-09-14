from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_pwd = [choice(letters) for l in range(randint(8, 10))]
    symbol_pwd = [choice(symbols) for s in range(randint(2, 4))]
    number_pwd = [choice(numbers) for n in range(randint(2, 4))]
    password_list = letter_pwd + symbol_pwd + number_pwd

    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def update_json(data):
    with open("data.json", "w") as file:
        # Writing the new data
        json.dump(data, file, indent=4)

        website_entry.delete(0, "end")
        password_entry.delete(0, "end")
        website_entry.focus()


def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
                "email": email,
                "password": password
            }
         }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            update_json(new_data)
        else:
            update_json(data)


# ---------------------------- SEARCH  ------------------------------- #
def search():
    try:
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS", message="No data file found")
    else:
        try:
            website = data[website_entry.get()]
        except KeyError:
            messagebox.showinfo(title="OOPS", message="No details for the website exists")
        else:
            email = website["email"]
            password = website["password"]
            messagebox.showinfo(title=website, message=f"email ID : {email}\n Password : {password}")




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas creation
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Label creation
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Username/Email:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry creation
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "premrajreddy16@gmail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

# Button creation
generate_pswd_button = Button(text="Generate Password", command=generate_password)
generate_pswd_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1)

window.mainloop()
