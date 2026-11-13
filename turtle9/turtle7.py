import turtle
turtle.shape('turtle')
turtle.speed(10)
turtle.bgcolor('black')


colors=['red', 'yellow', 'orange', 'blue', 'green']

for i in range(300):
    turtle.color(colors[i%5])
    turtle.forward(i*0.8)
    turtle.left(59)
