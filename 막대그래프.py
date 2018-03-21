
import turtle

t=turtle.Turtle()

data=[120,56,309,220,156,23,98]

def draw(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height),font=('Arial',16,'bold'))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

t.color('red')
t.fillcolor('blue')
t.pensize(3)
for d in data:
    draw(d)
