import turtle as t

def circle(x,y,color):
    #t.up()
    #t.goto(x,y)
    #t.down()
    #t.circle(100)
    #t.up()
    #t.goto(x,y+20)
    #t.down()
    #t.circle(80)

    t.up()
    t.goto(x,y)
    t.down()
    t.pensize(20)
    t.color(color)
    t.circle(100)


circle(-200,50,'blue')
circle(0,50,'black')
circle(200,50,'red')
circle(100,-50,'green')
circle(-100,-50,'yellow')
