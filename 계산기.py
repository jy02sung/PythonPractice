from tkinter import *

op=' '
temp_num=0
def button_press(value):
    E.insert('end',value)
    #print(value,'press') 쉘에서 버튼 불량 확인(?)

def Math(value):
    global op
    global temp_num
    if not E.get()=='':
        op=value
        temp_num=float(E.get())
        E.delete(0,'end')
        print(temp_num,op)

def clear_button():
    E.delete(0,'end')
    
def equal_button():
    global op
    global temp_num
    if not (op=='' and E.get()==''):
        num=float(E.get())
        if op =='/':
            result=temp_num/num
        elif op =='*':
            result=temp_num*num
        elif op =='+':
            result=temp_num+num
        elif op =='^':
            result=temp_num**num
        else:
            result=temp_num-num
        E.delete(0,'end')
        E.insert(0,result)
        print(temp_num,op,num,'=',result)
        
        op=' '
        temp_num=0
            
window=Tk()
window.title('꼐싼끼')
E=Entry(window,width=33,bg='black',fg='white')
E.grid(row=0, column=0, columnspan=5)

B1=Button(window,text='1',width=5,command=lambda:button_press('1'))
B2=Button(window,text='2',width=5,command=lambda:button_press('2'))
B3=Button(window,text='3',width=5,command=lambda:button_press('3'))
BC=Button(window,text='C',width=5,command=lambda:clear_button())
B4=Button(window,text='4',width=5,command=lambda:button_press('4'))
B5=Button(window,text='5',width=5,command=lambda:button_press('5'))
B6=Button(window,text='6',width=5,command=lambda:button_press('6'))
B7=Button(window,text='7',width=5,command=lambda:button_press('7'))
B8=Button(window,text='8',width=5,command=lambda:button_press('8'))
B9=Button(window,text='9',width=5,command=lambda:button_press('9'))
B0=Button(window,text='0',width=5,command=lambda:button_press('0'))
BE=Button(window,text='=',width=5,command=lambda:equal_button())
BP=Button(window,text='.',width=5,command=lambda:button_press('.'))
BD=Button(window,text='/',width=5,command=lambda:Math('/'))
BM=Button(window,text='*',width=5,command=lambda:Math('*'))
BA=Button(window,text='+',width=5,command=lambda:Math('+'))
BS=Button(window,text='-',width=5,command=lambda:Math('-'))
B17=Button(window,text='^',width=5,command=lambda:Math('^'))
B18=Button(window,text='',width=5,command=lambda:button_press(''))
B19=Button(window,text='',width=5,command=lambda:button_press(''))
B20=Button(window,text='',width=5,command=lambda:button_press(''))

B1.grid(row=1, column=0)
B2.grid(row=1, column=1)
B3.grid(row=1, column=2)
BA.grid(row=1, column=3)
BC.grid(row=1, column=4)
B4.grid(row=2, column=0)
B5.grid(row=2, column=1)
B6.grid(row=2, column=2)
BS.grid(row=2, column=3)
B18.grid(row=2, column=4)
B7.grid(row=3, column=0)
B8.grid(row=3, column=1)
B9.grid(row=3, column=2)
BM.grid(row=3, column=3)
B17.grid(row=3, column=4)
BP.grid(row=4, column=0)
B0.grid(row=4, column=1)
BE.grid(row=4, column=2)
BD.grid(row=4, column=3)
B19.grid(row=4, column=4)

window.mainloop()

