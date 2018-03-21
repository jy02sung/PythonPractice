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
        if y1<=0 or y2>=400:
            self.yspeed=-self.yspeed

window=Tk()
canvas=Canvas(window,width=800,height=400)
canvas.pack()

X=100
Y=random.randint(0,400)

bullets = []
def fire(event):
    bullets.append(Ball(canvas,'blue',10,X,Y,10,0))
canvas.bind('<Button-1>',fire)

ballE=Ball(canvas,'red',50,700,300,0,10)
#print('Ball color?',ballE.color)
#print('Ball Size?',ballE.size)
#print('Ball X?',ballE.x)
#print('')

ballA=Ball(canvas,'green',50,100,200,0,15)
#print('Ball color?',ballA.color)
#print('Ball Size?',ballA.size)
#print('Ball X?',ballA.x)
#print('')

while True:
    for bullet in bullets:
        bullet.move()
        if(bullet.x+bullet.size)>=800:
            canvas.delete(bullet.id)
            bullets.remove(bullet)
    ballE.move()
    ballA.move()
    window.update()
    time.sleep(0.03)
window.mainloop()
