import matplotlib.pyplot as plt

#collatz 
x = []
y = []
for a in range(5,10000):
    x.append(a)
    i=0
    while a !=1:
        i=i+1
        if a%2==0:
            a = a/2
        else:
            a = a*3 +1
    y.append(i)
print(max(y))
plt.scatter(x,y,s=1)
plt.show()

