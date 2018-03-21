import turtle as t
import turtle

t=turtle.Turtle()
s=turtle.Screen()

def square(length):
    for int in range(4):
        t.forward(length)
        t.left(90)

def draw(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color('blue')
    square(50)
    t.end_fill()


s.onscreenclick(draw)