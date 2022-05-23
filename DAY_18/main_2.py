from turtle import Turtle, Screen
import random

a_turtle= Turtle()
a_turtle.shape("arrow")
colors=["red","yellow","green","purple","black","orange"]


def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        a_turtle.forward(100)
        a_turtle.right(angle)


for shape in range(3,10):
    a_turtle.color(random.choice(colors))
    draw_shape(shape)

screen= Screen()
screen.exitonclick()