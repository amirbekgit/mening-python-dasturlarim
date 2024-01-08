from turtle import *

bgcolor('white')

chiziq = Turtle()
chiziq.pensize(10)
chiziq.color('blue')
chiziq.speed(0)
chiziq.up()
chiziq.goto(300, 300)
chiziq.down()
chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

square = Turtle()
square.shape('circle')
square.penup()
square.color('black')
square.goto(0, 0)


step_x = 3
step_y = 2

while True:
    x, y = square.position()

    if x + step_x >= 300 or x + step_x <= -300:
        step_x = -step_x
    if y + step_y >= 300 or y + step_y <= -300 :
        step_y = - step_y

    square.goto(x+step_x, y + step_y)