import turtle


t=turtle.Turtle()
s=turtle.Screen()

def Maze(x,y):
    for i in range(2):
        t.up()
        if i == 1:
            t.goto(x+150,y+100)
        else:
            t.goto(x,y)
        t.down()
        t.forward(300)
        t.right(120)
        t.forward(300)
        t.left(120)
        t.forward(300)

Maze(-300,0)

def turn_left():
    t.left(10)
    t.forward(10)

def turn_right():
    t.right(10)
    t.forward(10)

t.shape('turtle')
s.onkey(turn_left,'Left')
s.onkey(turn_right,'Right')

t.up()
t.goto(-300,50)
t.speed(1)
t.down()
s.listen()
s.mainloop()
