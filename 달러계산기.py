from tkinter import *


def change():
    E2.delete(0,END)
    F=float(E1.get())
    myC=F/1068.50
    E2.insert(0,str(myC))

def change2():
    E1.delete(0,END)
    C=float(E2.get())
    myF=C*1068.50
    E1.insert(0, str(myF))

window=Tk()

L1=Label(window,text='Won',font='verdana 16 bold')
L2=Label(window,text='Dollar',font='verdana 16 bold')
L1.grid(row=0,column=0)
L2.grid(row=1,column=0)

E1=Entry(window,bg='skyblue',fg='purple')
E2=Entry(window,bg='lime',fg='yellow')
E1.grid(row=0,column=1)
E2.grid(row=1,column=1)

B1=Button(window,text='Won->Dollar',command=change)
B2=Button(window,text='Dollar->Won',command=change2)
B1.grid(row=0,column=2)
B2.grid(row=1,column=2)

window.mainloop()