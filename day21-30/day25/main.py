import turtle
import sys
import os
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = os.path.join(sys.path[0], "blank_states_img.gif")
screen.addshape(image)

bg = turtle.Turtle(image)

states = pandas.read_csv(os.path.join(sys.path[0], "50_states.csv"))

state_to_formatted_state = {}
for s in states.state:
    state_to_formatted_state[s.lower()] = s

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed("fastest")

num_answered_states = 0

while num_answered_states < 50:
    answer_state = screen.textinput(
        title=f"{num_answered_states}/50 States Correct", prompt="What's another state's name?").lower()

    if answer_state == "exit":
        break

    if answer_state in state_to_formatted_state:
        formatted_state = state_to_formatted_state[answer_state]
        row = states[states.state == formatted_state].iloc[0]
        t.goto(row.x, row.y)
        t.write(row.state, align="center", font=("Arial", 8, "normal"))
        del state_to_formatted_state[answer_state]
        num_answered_states += 1

# store unanswered states to learn.csv
unanswered_states = state_to_formatted_state.values()
unanswered_states_df = states[states.state.isin(unanswered_states)]
unanswered_states_df.to_csv(os.path.join(sys.path[0], "learn.csv"))
