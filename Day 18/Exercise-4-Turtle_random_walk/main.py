from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ["medium blue", "dim gray", "medium turquoise", "forest green", "yellow", "red", "magenta", "blue violet"]
direction = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for n in range(500):
    tim.color(random.choice(colors))
    tim.forward(20)
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()
