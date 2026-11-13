import turtle

turtle.shape('turtle')
turtle.speed(50)
turtle.bgcolor('black')


colors=['red', 'yellow', 'orange', 'blue', 'green']

def flower(a):
    for i in range(a):
     turtle.color(colors[i%5])
     turtle.circle(100)
     turtle.right((i+1)*20)

  #a=int(input())
flower(400)
