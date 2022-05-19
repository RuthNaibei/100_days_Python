from turtle import Turtle, Screen

# creating an object from a class
jimmy = Turtle()
print(jimmy)

# obtaining a method from an object
jimmy.shape("turtle")
jimmy.color('yellow', 'red')
jimmy.forward(100)
my_screen = Screen()

# obtaining an attribute from an object

print(my_screen.canvheight)
my_screen.exitonclick()

# from prettytable import PrettyTable
#
# #object called table
# table = PrettyTable()
#
# table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmanda"])
# table.add_column("Type" ,["Electric","Water","Fire"])
#
# table.align="l"
#
# print(table)