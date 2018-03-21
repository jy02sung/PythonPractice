import turtle
import random

t1=turtle.Turtle()
t2=turtle.Turtle()

t1.shape('turtle')
t1.color('yellow')
t1.shapesize(2)
t1.pensize(5)
t1.up()
t1.goto(-300,0)
t1.down()
t1.speed(1)

t2.shape('turtle')
t2.color('green')
t2.shapesize(2)
t2.pensize(5)
t2.up()
t2.goto(-300,-200)
t2.down()
t2.speed(1)

for X in range(10):
    a = random.randint(1,10)
    t1.forward(a*10)
    b = random.randint(1,10)
    t2.forward(b*10)