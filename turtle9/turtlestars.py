import turtle

turtle.shape('turtle')
turtle.speed(5)
turtle.bgcolor('black')


colors=['red', 'yellow', 'orange', 'blue', 'green']

def star(n):
    for u in range(n):
     turtle.color(colors[u%4])
     turtle.forward(100)
     turtle.right(140)
     turtle.forward(100)
     turtle.left(140-360/n)
    
n=int(input())
star(n)

turtle.done
