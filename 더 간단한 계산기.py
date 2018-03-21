from tkinter import *

def BT(B):
    if B=='C':
        E.delete(0,'end')
    elif B=='D':
        E.delete('end')
    elif B=='=':
        result=eval(E.get())
        E.delete(0,'end')
        E.insert(0,result)
        
    else:
        E.insert('end',B)

window=Tk()
window.title('꼐싼끼 2.0')
E=Entry(window,bg='black',fg='white')
E.pack(pady=5)
E.insert(0, '')

buttons=['147.','2580','369=','+-*/','C^% ']

for col in buttons:
    frame=Frame(window)
    frame.pack(side=LEFT)
    for row in col:
        B=Button(frame, text=row, command=(lambda char=row:BT(char)))
        B.pack(fill=X, padx=5, pady=5)

frame.bind('<Enter>', BT(=))
window.mainloop()
