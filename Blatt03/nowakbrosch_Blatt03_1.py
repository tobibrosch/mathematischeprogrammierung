import math

#a

A = {(i,math.sqrt(i)) for i in range(1,26)}

#print(A)

#b

a=1
b=10
n=18

lst = [a+i*((b-a)/n) for i in range(n)]

#print(lst)

#c

C = {i for i in range(1,11)}

menge_c = {(a,b) for a in C for b in C if a!=b and (a/b)%1==0}

#print(menge_c)

#d

D = {i for i in range(1,8)}

def betqua(x,y):
    return math.sqrt(x**2+y**2)
    
menge_d = {(a,b,int(betqua(a,b))) for a in D for b in D if betqua(a,b)<=7 and betqua(a,b)%1==0}

#print(menge_d)
















