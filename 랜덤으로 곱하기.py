import random

a=int(input('First Num:'))
b=int(input('Second Num:'))
for x in range(1,4):
    s=random.randint(1,3)
    if s==1:
        print('A+B=', a+b)
    elif s==2:
        print('A-B=', a-b)
    else:
        print('A*B=', a*b)
