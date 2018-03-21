import turtle as t

#turtle
t.shape('turtle')






a=input('몇각형?')
z=int(a)
for x in range(z):
    t.forward(100)
    t.left(360/z)
