def prime(n):
    if n==1:
        return False
    i=2
    while i<n:
        if n%i==0:
            return False
        i+=1
    return True

num=200

i=1
while i<=num:
    if num%i==0 and prime(i):
        print(i,'is prime')
    i+=1
