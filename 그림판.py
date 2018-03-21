from tkinter import *

window=Tk()

Color='black'


def paint(event):
    x1,y1=(event.x-2),(event.y+2)
    x2,y2=(event.x-2),(event.y+2)
    canvas.create_oval(x1,y1,x2,y2,fill=Color,outline=Color)

def change():
    global Color
    Color='red'
    canvas.delete('all')


window.geometry('600x600')
canvas=Canvas(window)
canvas=Canvas(window, width=600, height=600)
canvas.pack()
canvas.bind('<B1-Motion>',paint)
B=Button(window,bg='red',command=change, width=4, height=3)
B.place(x=0,y=0)
window.mainloop()
