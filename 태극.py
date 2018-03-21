import turtle

t=turtle.Turtle()

def circle(radius, color):
    t.left(270)
    t.color('black',color)
    t.begin_fill()
    t.circle(radius/2,-180)
    t.circle(radius,180)
    t.left(180)
    t.circle(-radius/2,-180)
    t.end_fill()

t.reset()
circle(200,'red')
t.setheading(180)
circle(200,'blue')

def square(x,y,xx,yy):
    t.up()
    t.goto(x,y)
    t.down()
    for int in range(2):
        t.forward(xx)
        t.left(90)
        t.forward(yy)
        t.left(90)
t.setheading(-45)
square(150,100,100,30)
