#!/usr/bin/python3
import turtle
turtle.shape("turtle")

def sq(a):
    for i in range (4):
        turtle.forward(a)
        turtle.left(90)

turtle.speed(5)

sq(100)

