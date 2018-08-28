# This program takes inputs as number of sides and length of side to give output as a symterical object with small versions of that
# object insede it
import turtle
sides = int(input('Enter number of sides you want to be drawn: '))
length = float(input('Enter length of each side: '))
for steps in range(sides):
    turtle.forward(length)
    turtle.right(360/sides)
    for steps in range (sides):
        turtle.forward(length/2)
        turtle.right(360/sides)
