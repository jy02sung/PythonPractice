from tkinter import *
import time
import random

class Ball:
    def __init__(self,canvas,color,size,x,y,xspeed,yspeed):
        self.canvas=canvas
        self.color=color
        self.size=size
        self.x=x
        self.y=y
        self.xspeed=xspeed
        self.yspeed=yspeed
        self.id=canvas.create_oval(x,y,x+size,y+size,fill=color)

    def move(self):
        self.canvas.move(self.id,self.xspeed,self.yspeed)
        (x1,y1,x2,y2)=self.canvas.coords(self.id)
        (self.x,self.y)=(x1,y1)
        if x1<=0 or x2>=800:
            self.xspeed=-self.xspeed
        if y1<=0 or y2>=800:
            self.yspeed=-self.yspeed

window=Tk()
canvas=Canvas(window,width=800,height=800)
canvas.pack()

color_list=['yellow','green','purple','blue','white']
balls_list=[]

for x in range(5):
    color=random.choice(color_list)
    size=random.randint(10,100)
    X=random.randint(1,20)
    Y=random.randint(1,20)
    XS=random.randint(1,10)
    YS=random.randint(1,10)
    balls_list.append(Ball(canvas,color,size,X,Y,XS,YS))

ballE=Ball(canvas,'red',50,30,30,XS,YS)
#print('Ball color?',ballE.color)
#print('Ball Size?',ballE.size)
#print('Ball X?',ballE.x)
#print('')

#ballA=Ball('red',30,50,50,10,10)
#print('Ball color?',ballA.color)
#print('Ball Size?',ballA.size)
#print('Ball X?',ballA.x)
#print('')

while True:
    for ball in balls_list:
        ball.move()
    ballE.move()
    window.update()
    time.sleep(0.03)