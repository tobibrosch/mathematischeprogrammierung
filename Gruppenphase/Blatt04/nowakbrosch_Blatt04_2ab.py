import numpy as np

print("\na)\n")
p = lambda x : x**i
basis = [lambda x, i=j : x**i for j in range(4)]
for k in range(3):
    print(basis[k](2)) 

print("\nb)\n")

def vandermonde_matrix(x,baselist):
    if len(x)==len(baselist):
        matrix = []
        for j in range(len(x)):
            matrix_row=[]
            for i in range(len(x)):
                matrix_row.append(baselist[i](x[j]))
            matrix.append(matrix_row)
        return matrix
    else:
        print("Stützstellenanzahl muss Basisfunktionenanzahl")

#Hier wird die Basisfunktionenliste angegeben
baselist = [lambda x : 1, lambda x : x,lambda x : x**2,lambda x : x**3]  
#Hier werden die Stützstellen als Tupel angegeben
x = (0,2,1,0.5)


A = vandermonde_matrix(x,baselist)
print(A)