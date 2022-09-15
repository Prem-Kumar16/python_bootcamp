from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}
# ----------------------------- READING FROM CSV ---------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    french_words_list = data.to_dict(orient="records")
    print("Using french words file")
else:
    french_words_list = data.to_dict(orient="records")
    print("Using words to learn file")


def next_card():
    global CURRENT_CARD, timer
    window.after_cancel(timer)
    CURRENT_CARD = random.choice(french_words_list)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=CURRENT_CARD["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    timer = window.after(3000, flip)


# ----------------------------------- FLIP CARDS -------------------------------------- #

def flip():
    global CURRENT_CARD
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=CURRENT_CARD["English"], fill="white")


# ---------------------------------- SAVING UNKNOWN DATA -------------------------------- #

def if_right():
    global CURRENT_CARD
    french_words_list.remove(CURRENT_CARD)
    new_data = pandas.DataFrame(french_words_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------- UI -------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, flip)

# Canvas

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=if_right)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
