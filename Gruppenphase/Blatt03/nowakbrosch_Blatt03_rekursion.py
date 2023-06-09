i=0
Fib = [1,1]
n = int(input("Welche Fibonaccizahl willst du?="))
while i < n:
    fib = Fib[i]+Fib[i+1]
    Fib.append(fib)
    i=i+1
print(f"Die Fibonacci Zahl F_{i+1} ist = {Fib[i]}")
print(Fib)
a=1
b=1
fibo=0
i=0
while i < n:
    fibo=a+b
    a=b
    b=fibo
    i=i+1
print(fibo)
def f(p):
    if p==1:
        return 1
    else:
        return f(p-1)*p 
        
print(f(10))