import random

A=random.randint(1,10)

while True:
    B=int(input('맞춰봐'))
    if(A>B):
        print('Too Small')
    elif(A<B):
        print('Too Big')
    else:
        print('Correct!')
        break

