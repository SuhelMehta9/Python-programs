# This program takes input as angle, line colour, line length to give output
import turtle
print('If you want to stop drawing please enter 0')
print('In case of angle the rotation will be from right of the arrow.')
length = 10
while length !=0:
    length = float(input('Please enter the length of the line: '))
    if length != 0:
        colour = input('Enter colour like pink, red, voilet etc: ')
        angle = float(input('Enter angle between 0 to 360: '))
        turtle.color(colour)
        turtle.right(angle)
        turtle.forward(length)
print('You are a good artist!')
