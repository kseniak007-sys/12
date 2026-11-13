#!/usr/bin/python3
import turtle
turtle.shape("turtle")

def sq(a):
    for i in range (4):
        turtle.color(colors[i%3])
        turtle.forward(a)
        turtle.left(90)

colors = ['black','blue','red']
turtle.speed(15)

b=50
for i in range(60):
    sq(b)
    turtle.right(15)
    b=b+5
