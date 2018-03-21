def calculate():
    result = 3.14*r**2
    return result

r = float(input('원의 반지름:'))
area = calculate()
print(area)