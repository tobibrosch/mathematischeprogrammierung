def f(n): 
    if n==1:
        return 3
    if n>1:
        return f(n-1)+3 
print(f(4))

def z(n):
    if n==0:
        return 1000
    if n>0:
        return z(n-1)*1.05

print(z(2))
import math
def df(n):
    if n==0:
        return 1
    if n==1:
        return 1
    elif n>1:
        return n*df(n-2)
print(df(8))

def inf(n,k): #k-fache Fakultät
    if n==0:
        return 1
    if n<=k and n>0:
        return n
    if n>k and k>0:
        return n*inf(n-k,k)
print(inf(9,3))

