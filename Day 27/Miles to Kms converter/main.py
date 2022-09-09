from tkinter import *
window = Tk()
window.title("My first GUI program")
window.minsize(width=350, height=200)
window.config(padx=30, pady=30)


def button_click():
    mile = int(inputs.get())
    result = round(mile * 1.6)

    ans = Label(text=result, font=("Courier", 12, "normal"))
    ans.grid(column=1, row=1)
    ans.config(padx=10, pady=10)


# Label

my_label = Label(text="is equal to", font=("Courier", 12, "normal"))
my_label.grid(column=0, row=1)
my_label.config(padx=10, pady=10)

miles = Label(text="Miles", font=("Courier", 12, "normal"))
miles.grid(column=2, row=0)
miles.config(padx=10, pady=10)

km = Label(text="Kmph", font=("Courier", 12, "normal"))
km.grid(column=2, row=1)
km.config(padx=10, pady=10)


# Entry

inputs = Entry(width=10)
inputs.grid(column=1, row=0)

# Buttons

button = Button()
button.config(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()
