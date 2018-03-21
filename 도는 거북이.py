import turtle as t
import random

t.shape('turtle')
t.speed(1)
t.color('green')


for x in range(500):
    A=random.randint(1,360)
    t.setheading(A)
    t.forward(10)
