from turtle import Turtle, Screen

a_turtle= Turtle()
a_turtle.shape("arrow")



for _ in range(10):
    a_turtle.forward(10)
    a_turtle.penup()
    a_turtle.forward(10)
    a_turtle.pendown()
screen= Screen()
screen.exitonclick()