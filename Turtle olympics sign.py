# This program will give output as a olympic sign and functions are used here.

import turtle

def circle():
	for steps in ['blue', 'black', 'red']:
		turtle.color(steps)
		turtle.circle(50)
		turtle.up()
		turtle.forward(120)
		turtle.down()
	return
  
def circle2():
	for steps in ['yellow', 'green']:
		turtle.color(steps)
		turtle.circle(50)
		turtle.up()
		turtle.forward(120)
		turtle.down()
	return
  
turtle.up()
turtle.backward(120)
turtle.down()

circle()

turtle.up()
turtle.backward(300)
turtle.right(90)
turtle.forward(30)
turtle.left(90)
turtle.down()

circle2()
