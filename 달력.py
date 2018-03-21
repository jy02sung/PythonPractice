A=int(input('?'))
if A % 4 == 0 and A % 100 !=0 or A % 400 == 0:
    print(A,'년은 윤년입니다~')
else:
    print(A,'년은 평년입니다~')
