import turtle
turtle.shape('turtle')
turtle.speed(10)
turtle.left(90)
turtle.width(3)
turtle.bgcolor('black')

colors=['red', 'yellow', 'orange', 'blue', 'green']

def cir(a):
    for i in range (a):
        turtle.color(colors[i%5])
        for m in range(2):
            turtle.circle((i+1)*20)
            turtle.right(180)

a=int(input())

cir(a)
