from tkinter import *

window=Tk()

L1=Label(window,text='성명')
L2=Label(window,text='회사명')
L3=Label(window,text='특징')
L1.grid(row=0,column=0)
L2.grid(row=1,column=0)
L3.grid(row=2,column=0)

E1=Entry(window)
E2=Entry(window)
E3=Entry(window)
E1.grid(row=0,column=1)
E2.grid(row=1,column=1)
E3.grid(row=2,column=1)

B=Button(window)
B.grid(row=3,column=0)

window.mainloop()