import turtle

turtle.shape('turtle')
turtle.speed(10)
turtle.bgcolor('black')

colors=['red','blue', 'white', 'yellow']

         
for i in range(400):
    turtle.color(colors[i%4])
    turtle.forward(i*0.3)
    turtle.left(10)
