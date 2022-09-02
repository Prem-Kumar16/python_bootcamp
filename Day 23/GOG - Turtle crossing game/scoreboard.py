from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.level_table()

    def level_table(self):
        self.goto(x=-200, y=250)
        self.write(arg=f"Level : {self.level}", align="center", font=FONT)

    def new_level(self):
        self.level += 1
        self.clear()
        self.level_table()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="Game Over!", align="center", font=FONT)
