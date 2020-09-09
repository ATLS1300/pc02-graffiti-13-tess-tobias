#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:40:38 2020

@author: oliviakokes
"""

#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Olivia Kokes
Sepetember 9, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 


image = "Bezos.gif"
panel.bgcolor("IndianRed")
panel.bgpic(image)


Turtle() #creating turtle to draw on

speed(7)

shape('arrow')
turtlesize(1)

# thick line
up() # pick up pen (stops drawing)
color("lavender")
width(12)
up() # pick up pen (stops drawing)
goto(360,245) # goes to x,y coordinate
down() # drop pen (starts drawing)
goto(100,0) # goes to x,y coordinate
goto(365,-245) # goes to x,y coordinate

# thin line
up()
color('SeaGreen')
width(4)
down() # drop pen (starts drawing)
goto(-365,-247) # goes to x,y coordinate
up()

# circle 
goto(-235,120)
color("turquoise4")
width(10)
down() # drop pen (starts drawing)
circle(50)
up() # pick up pen (stops drawing)

# polygon
goto(-240,-160)
color("MediumPurple4")
right(45)
down() # drop pen (starts drawing)
forward(60) # forward 60 pixels
left(90)
forward(60) # forward 60 pixels
left(90)
forward(60) # forward 60 pixels
left(90)
forward(60) # forward 60 pixels
end_poly()
up()

# new shape
goto(250,-200) # goes to x,y coordinate
color('magenta')
shape('turtle')
shapesize(stretch_wid=5, stretch_len=5)















































