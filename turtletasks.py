a = int(input("enter 1 side of triangle: "))
b = int(input("enter 2 side of triangle: "))
c = int(input("enter 3 side of triangle: "))
u = (a+b+c)/2
import math
A = math.sqrt(u*(u-a)*(u-b)*(u-c))
print(A)

x = int(input("enter variable: "))
y = (x**2-3*x+2)/(math.sqrt(2*x**3-1))
print(y)





x = int(input())
if x > 100:
    print("over")
else: print('less')

y = int(input('enter year of your birth\n'))
if 2021-y<=3:
    print('baby')
else: print('oldman')

for i in range(1,101,10):
    print(i)

#square
    import turtle as tur 
t = tur.Turtle()
for i in range(1,4,1):
    t.forward(100)
    t.left(90)
tur.done()

#star
import turtle as tur 
t = tur.Turtle()
for i in range(0,6,1):
    t.forward(100)
    t.left(144)
tur.done()


#6angle
import turtle as tur 
t = tur.Turtle()
for i in range(0,6,1):
    t.forward(100)
    t.left(60)
tur.done()



import turtle as tur 
t = tur.Turtle()
for i in range(0,40,1):
    t.left(18)
    for i in range(4):
      t.forward(100)
      t.left(90)
    
tur.done()

# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()