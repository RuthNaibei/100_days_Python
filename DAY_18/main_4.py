# import colorgram
#
# colors = colorgram.extract('hirst.jpeg',30)
# rgb_colors=[]
#
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color= (r,g,b)
#     rgb_colors.append(new_color)
#
import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
t=Turtle()
screen= Screen()
color_list=[(247, 242, 234), (237, 242, 248), (249, 240, 244), (239, 247, 244), (139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89), (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166), (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193), (166, 200, 213)]

num_of_dots=100
t.speed(("fastest"))
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)


for dot_count in range(1,num_of_dots+1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot_count%10==0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()