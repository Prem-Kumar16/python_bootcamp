from turtle import Turtle

SCORE = 0
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score : {SCORE}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        global SCORE
        SCORE += 1
        self.clear()
        self.update_score()
