from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Canvas creation
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="bla bla bla bla", fill=THEME_COLOR, width=280,
                                                     font=("Arial", 12, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        # Score text
        self.score_label = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Buttons
        self.tick_img = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=self.tick_img, highlightthickness=0, command=self.tick_click)
        self.tick_button.grid(column=0, row=2)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false_click)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score : {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\n"
                                                            f"Your final score "
                                                            f"was {self.quiz.score}/{self.quiz.question_number}")
            self.tick_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def tick_click(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_click(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
            self.canvas.update()
        else:
            self.canvas.config(bg="red")
            self.canvas.update()

        self.window.after(1000, self.get_next_question)

