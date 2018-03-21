n=0
a=0
b=1
while a<=4000000:
    if a%2==0:
        n+=a
    a,b=b,a+b
print(n)
