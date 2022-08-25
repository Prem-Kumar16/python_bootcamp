from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["medium blue", "dim gray", "medium turquoise", "forest green", "yellow", "red", "magenta", "blue violet"]
tim.shape("turtle")
tim.color("DarkMagenta")

for n in range(3, 11):
    tim.color(random.choice(colors))
    for i in range(0, n):
        tim.forward(100)
        tim.left(360/n)

screen = Screen()
screen.exitonclick()
