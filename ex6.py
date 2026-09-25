#!/usr/bin/python3
n=int(input())

import turtle
turtle.shape('turtle')
turtle.speed(100)
for i in range(n):
    turtle.forward(80)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(80)
    turtle.right(180)
    turtle.left(360/n)
