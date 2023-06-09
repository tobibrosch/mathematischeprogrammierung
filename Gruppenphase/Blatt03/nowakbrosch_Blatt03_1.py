import math

#a

A = [(i,math.sqrt(i)) for i in range(1,26)]

print(f"Aufgabe a.){A}")

#b3

a=1
b=10
n=18

lst = [a+i*((b-a)/n) for i in range(n)]

print(f"Aufgabe b.) {lst}")

#c

C = {i for i in range(1,11)}

menge_c = {(a,b) for a in C for b in C if a!=b and (a/b)%1==0}

print(f"Aufgabe c.) {menge_c}")

#d

D = {i for i in range(1,8)}

menge_d = {(a,b,r) for a in D for b in D for r in D if a**2+b**2==r**2}

print(f"Aufgabe d.) {menge_d}")





