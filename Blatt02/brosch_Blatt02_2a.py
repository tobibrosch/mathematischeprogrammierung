import math
x=2
h=0.1
x_h=x+h
sin_dx=(math.sin(x_h)-math.sin(x))/h
print("Der Differenzenquotient von sin'(",x, ") ist bei = ",sin_dx)

e_x=abs(math.cos(x)-sin_dx)
print("Der Fehler für h =",h,"ist bei =",e_x)
