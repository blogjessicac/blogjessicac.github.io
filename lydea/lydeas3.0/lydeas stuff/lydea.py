from turtle import *
from random import *
colormode(255)

def randomcolor():
 red = randint(0, 255)
 green = randint(0, 255)
 blue = randint(0, 255)
 color(red,green,blue)

def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint (-100, 100)
    goto(x, y)
    pendown()

def randomheading():
    z=randint(0, 360)
    ranint(z)

shape('circle')

for i in range(30):
    randomplace()
    randomcolor()
    randomheading()
    stamp()
