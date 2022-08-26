from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which color do you think will win the race?").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtles in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    y_co = (-150 + (turtles * 50))
    new_turtle.goto(x=-230, y=y_co)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        x_cor = turtle.xcor()
        if x_cor > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"Hurrah, you & your bet turtle {winner} has won")
            else:
                print(f"Sorry, the {winner} colored turtle actually won")

screen.exitonclick()
