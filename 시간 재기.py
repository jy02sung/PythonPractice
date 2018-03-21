import time

FirstEnter=input('FirstEnter')
FirstTime=time.time()

SecondEnter=input('SecondEnter')
SecondTime=time.time()

Time=int(SecondTime)-int(FirstTime)
print('실제시간:',Time,'초')
print('시간차이:',abs(Time-20),'초')
