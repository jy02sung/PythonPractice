import turtle

t=turtle.Turtle()
s=turtle.Screen()

def draw(x,y):
    t.pensize(3)
    t.goto(x,y)
    t.color('blue')

s.onscreenclick(draw)   
