import turtle
from turtle import Turtle, Screen
import random

a_turtle = Turtle()
turtle.colormode(255)
a_turtle.shape("arrow")

directions = [0, 90, 180, 270]



def color_type():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


a_turtle.speed("fastest")


def draw_spirograph(space_of_circle):
    for _ in range(int(360/space_of_circle)):
        a_turtle.color(color_type())
        a_turtle.circle(100)
        current_heading = a_turtle.heading()
        a_turtle.setheading(current_heading + space_of_circle)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
