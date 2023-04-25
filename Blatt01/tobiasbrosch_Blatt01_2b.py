import math
x = float(input("Wähle x="))
k = int(input("Wähle k-Summand="))
sin_x=0
for i in range (0, k):  
    sin_x=sin_x+(-1)**(i)*(x**(2*i+1))/math.factorial(2*i+1)
print("sinus(",x ,")=",sin_x)