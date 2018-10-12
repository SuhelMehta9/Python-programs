# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:47:36 2018

@author: Suhel
"""

import graphics
import random
import boardgame
import time

fps  = 1
start_life = 6
#start_live = int(input("Enter number of live cells: "))

# This will define how many blocks will be there on x-axis
x_scale = 40

win_max=1000

tickrate = 1/fps

ticker = tickrate

# scale variable is for the length of each block or square
scale = round(win_max/x_scale)

colour = graphics.color_rgb(150,200,250)
#print(colour)



win = graphics.GraphWin('Game of life',win_max,win_max)

blocks = []
neighbours = 0

# This loop creates boundary of the square where cell will live or die
for x_axis in range(scale, win_max +1, scale):
    
    for y_axis in range(scale, win_max +1, scale):

        point1 = graphics.Point(x_axis, y_axis)
        point2 = graphics.Point(x_axis - scale, y_axis - scale)
        
        block = [graphics.Rectangle(point1, point2), "dead", neighbours, "die"]

        block[0].draw(win)
        
        blocks.append(block)


while start_life > 0:
    mouse = win.getMouse()
    mouse_x = mouse.getX()
    mouse_y = mouse.getY()
    for index in range(0, len(blocks)):

        center = blocks[index][0].getCenter()
        
        center_x = center.getX()
        
        center_y = center.getY()
        

        if abs(center_x - mouse_x) < scale/2:

            if abs(center_y - mouse_y) < scale/2:
                
                # When we click on a cell then it's colour must change and it must be alive instead of dead
                blocks[index][0].setFill(colour)
                blocks[index][1] = "alive" # Replacing dead with alive in block
    
    start_life -= 1

boardgame.indexing(blocks, x_scale)

while True:
    if time.clock() > ticker :
        for index in range(0,len(blocks)):
            for x in blocks[index][4]:
                if blocks[x][1] == "alive":

                    blocks[index][2] += 1
            if blocks[index][1] == "alive":
                # if neighbours of live cell is 2 or 3 then new cell will born
                if blocks[index][2] > 1 and blocks[index][2] < 4:

                    blocks[index][3] = "born"

                else:

                    blocks[index][3] = "die"

            elif blocks[index][1] == "dead":

                if blocks[index][2] == 3:

                    blocks[index][3] = "born"
        

                else:

                    blocks[index][3] = "die"

            blocks[index][2] = 0


        for index in range(0, len(blocks)):

            blocks[index][2] = 0

            if blocks[index][3] == "born":
                
                blocks[index][1] = "alive"
                blocks[index][0].setFill(color)

            else:
                blocks[index][1] = "dead"
                blocks[index][0].setFill("white")

            blocks[index][3] = "die"

        ticker += tickrate

