from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, co_or):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(co_or)

    def up(self):
        y_pos = self.ycor()
        self.goto(y=y_pos + 20, x=self.xcor())

    def down(self):
        y_pos = self.ycor()
        self.goto(y=y_pos - 20, x=self.xcor())
