num=0

for x in range(1,1000):
    if x%3==0 or x%5==0:
        num+=x
        #num=num+x랑 같음
print(num)
