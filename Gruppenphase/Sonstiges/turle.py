import turtle as tut
from math import sin, cos
import time


def fib(i):
    if i == 0:
        return 1
    if i == 1: 
        return 1 
    if i > 1:
        return fib(i-1)+fib(i-2)

for i in range(15):
      tut.circle(fib(i)/2,180)

#tut.speed(0)
#for i in range(2300):
#    tut.goto(200*sin(i/50)*cos(i/50*2/5),200*cos(2/5*i/50)*cos(i/50))
#tut.exitonclick()



