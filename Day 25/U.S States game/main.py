import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S States game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0
states = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while game_is_on:

    # Covert the answer text to title case
    answer = screen.textinput(title=f"{score}/50 states correct", prompt="What's the other state name?").title()

    # Check if the gamer has scored the total points i.e., 50 in this case
    if score == 50 or answer == "Exit":
        game_is_on = False
    else:

        # Check if the guess is among 50 states
        for state in data["state"]:
            if answer == state:
                # Get x & y coordinates
                row = data[data.state == answer]
                xcor = int(row.x)
                ycor = int(row.y)
                # print(xcor, ycor)

                # Create a turtle to write state name
                tim = turtle.Turtle()
                tim.penup()
                tim.hideturtle()
                tim.goto(x=xcor, y=ycor)
                tim.write(arg=answer, align="center")

                # Increase the score by 1
                score += 1

                # Append the answer to a list
                states.append(answer)

# Make a .csv file for the states to learn
unknown_states = []

for state in all_states:
    if state not in states:
        unknown_states.append(state)

print("Unknown states")
print(unknown_states)
new_data = pandas.DataFrame(unknown_states)
new_data.to_csv("Unknown_states.csv")
print("Known states")
print(states)


