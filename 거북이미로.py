import turtle

t=turtle.Turtle()

def Maze(x,y):
    for i in range(2):
        t.up()
        if i == 1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)
        t.down()
        for a in range(2):
            if a == 1:
                t.forward(200)
                t.left(90)
                t.forward(200)
            else:
                t.forward(200)
                t.right(90)
    t.up()
                

Maze(-300,200)

t=turtle.Turtle()
s=turtle.Screen()

def draw(x,y):
    t.up()
    t.speed(1)
    t.goto(x,y)

s.onscreenclick(draw)
