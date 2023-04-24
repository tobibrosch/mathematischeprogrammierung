import math
x=2
for i in range(1,16):
    h=10**(-i)
    x_h=x+h
    sin_dx=(math.sin(x_h)-math.sin(x))/h
    e_x=abs(math.cos(x)-sin_dx)
    print("Für ", h , "ist der Fehler bei=", e_x)