#!/usr/bin/python3
import turtle
turtle.shape('turtle')
for i in range(100,1000,100):
            for m in range(4):
                        turtle.forward(i)
                        turtle.left(90)
            turtle.penup()
            for m in range (2):
                        turtle.right(90)
                        turtle.forward(50)
            turtle.pendown()
            turtle.right(180)


