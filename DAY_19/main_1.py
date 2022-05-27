from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle is going to win the race?Enter a color: ")
colors = ["yellow", "red", "black", "purple", "orange", "blue"]
all_turtles = []
y_positions = [-70, -30, 10, 50, 90, 130]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. {winning_color}")
            else:
                print(f"You have lost winner is {winning_color}")
        race_distance = random.randint(0, 10)
        turtle.forward(race_distance)
screen.exitonclick()
