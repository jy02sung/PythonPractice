from tkinter import *


def change():
    F=float(E1.get())
    myC=(F-32)*5/9
    E2.insert(0,str(myC))

def change2():
    C=float(E2.get())
    myF=(C*9/5)+32
    E1.insert(0, str(myF))

window=Tk()

L1=Label(window,text='화씨')
L2=Label(window,text='섭씨')
L1.grid(row=0,column=0)
L2.grid(row=1,column=0)

E1=Entry(window)
E2=Entry(window)
E1.grid(row=0,column=1)
E2.grid(row=1,column=1)

B1=Button(window,text='화씨->섭씨',command=change)
B2=Button(window,text='섭씨->화씨',command=change2)
B1.grid(row=0,column=2)
B2.grid(row=1,column=2)

window.mainloop()