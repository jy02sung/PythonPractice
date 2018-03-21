import turtle as t
import random

tv=t.Turtle()
tf=t.Turtle()
score=0
playing=False

tv.shape('turtle')
tv.color('red')
tv.up()
tv.goto(0,200)
tv.speed(1)

t.setup(500,500)
t.bgcolor('orange')
t.shape('turtle')
t.color('green')
t.up()
t.speed(1)

tf.shape('circle')
tf.color('yellow')
tf.up()
tf.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_left():
    t.setheading(180)

def turn_up():
    t.setheading(90)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if playing == False:
        playing=True
        t.clear()
        play()

def play():
    global score
    global playing
    t.forward(10)
    if random.randint(1,5)==3:
        t_angle=tv.towards(t.pos())
        tv.setheading(t_angle)
        speed=score+1
        if speed>15:
            speed=15
        tv.forward(speed)
    if t.distance(tf)<12:
        score=score+1
        t.write(score)
        move_x=random.randint(-230,230)
        move_y=random.randint(-230,230)
        tf.goto(move_x,move_y)
    if t.distance(tv)<12:
        text='Score:' + str(score)
        message("Game Over",text)
        playing=False
        score=0
    if playing:
        t.ontimer(play,100)

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,'center',("",20))
    t.goto(0,-100)
    t.write(m2,False,'center',("",15))
    t.home()

t.title('Turtle Run')
t.onkeypress(turn_right,'d')
t.onkeypress(turn_left,'a')
t.onkeypress(turn_up,'w')
t.onkeypress(turn_down,'s')
t.onkeypress(start,'space')
t.listen()
message('Turtle Run', '[Space]')
