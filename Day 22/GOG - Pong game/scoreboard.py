from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.point_table()

    def point_table(self):
        self.clear()
        self.goto(-100, 270)
        self.write(arg=self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 270)
        self.write(arg=self.r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.point_table()

    def r_point(self):
        self.r_score += 1
        self.point_table()
