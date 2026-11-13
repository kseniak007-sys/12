#!/usr/bin/python3

import turtle
turtle.shape('turtle')
turtle.speed(10)
def roo(n):
    angle= (n-2)*180
    if angle%n==0:
        angle1=angle//n
        for i in range (n):
            turtle.forward(n*10)
            turtle.left(180-angle1)
        for i in range (1):
            turtle.penup()
            turtle.right(90)
            turtle.forward(10)
            turtle.left(90)
            turtle.pendown()
for i in range (3,10):
    roo(i)
