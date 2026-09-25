#!/usr/bin/python3
import turtle
turtle.shape('turtle')

for i in range(10,100,10):
            turtle.forward(i)
            turtle.left(90)
            turtle.forward(i)
            turtle.left(90)
            turtle.forward(i)
            turtle.left(90)
            turtle.forward(i)
            turtle.left(90)
            turtle.penup()
            turtle.right(90)
            turtle.forward(5)
            turtle.right(90)
            turtle.forward(5)
            turtle.pendown()
            turtle.left(180)


