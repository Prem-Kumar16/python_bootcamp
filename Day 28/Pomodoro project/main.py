from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    label_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label_tick.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="Break", fg=PINK)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    count_min = math.floor(count / 60)
    count_sec = round(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS / 2)
        for n in range(work_sessions):
            mark += "✔"
        label_tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label_title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(column=1, row=0)

label_tick = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
label_tick.grid(column=1, row=3)

start_button = Button()
start_button.config(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()