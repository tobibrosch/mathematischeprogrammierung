import math
x=2
h=0.1
x_h=x+h
sin_dx=(math.sin(x_h)-math.sin(x))/h
print(f"Der Differenzenquotient von sin'({x}) ist bei = {sin_dx}")

e_x=abs(math.cos(x)-sin_dx)
print(f"Der Fehler für h = {h} ist bei = {e_x}")