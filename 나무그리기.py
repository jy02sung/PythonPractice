import turtle

t=turtle.Turtle()

def tree(length):
    if length > 5:
        t.forward(length)
        t.right(20)
        tree(length-18)
        t.left(40)
        tree(length-18)
        t.right(20)
        t.backward(length)

t.left(90)
t.color('green')
t.speed(0)
tree(100)