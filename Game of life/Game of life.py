# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 00:08:20 2018

@author: Chintu
"""

import graphics
import random
import boardgame
import time

x_scale = 50

# This will make a window in which we will see a input and output
win_max = 500

# Take input as number of living cells
start_lives = int(input('Enter number of live cells or living cells that you want to add: '))

# fps is frame per second
fps = 1
color = graphics.color_rgb(125, 200, 100)

tickrate = 1/fps

scale = round(win_max/x_scale)

ticker = tickrate
blocks = []
neighbours = 0


win = graphics.GraphWin("Game Of Life", win_max, win_max)

for cut in range(scale, win_max +1, scale):

    for cut2 in range(scale, win_max +1, scale):

        point1 = graphics.Point(cut, cut2)
        point2 = graphics.Point(cut - scale, cut2 - scale)
        
        block = [graphics.Rectangle(point1, point2), "dead", neighbours, "die"]

        block[0].draw(win)

        blocks.append(block)


# This loop is for input
while start_lives > 0:

    mouse = win.getMouse()
    mouse_x = mouse.getX()
    mouse_y = mouse.getY()

    for index in range(0, len(blocks)):

        center = blocks[index][0].getCenter()
        
        center_x = center.getX()
        
        center_y = center.getY()
        

        if abs(center_x - mouse_x) < scale/2:

            if abs(center_y - mouse_y) < scale/2:

                blocks[index][0].setFill(color)
                blocks[index][1] = "alive"
                
                start_lives -= 1
                

boardgame.indexing(blocks, x_scale)

while True:

    if time.clock() > ticker :

        for index in range(0, len(blocks)):

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