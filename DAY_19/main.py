from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_counterclockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_clockwise():
    tim.right(-90)


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.listen()
screen.exitonclick()
