import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirograph(gap):
    degree = int(360/gap)
    for n in range(degree):
        tim.color(random_colors())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + gap)


draw_spirograph(1)

screen = t.Screen()
screen.exitonclick()

