from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("DarkMagenta")

for n in range(10):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()
