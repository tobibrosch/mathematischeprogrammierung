import numpy as np

print("\na)\n")
p = lambda x : x**i
basis = [p for i in range(4)]
for i in range(3):
    print(basis[i](2)) 

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


A1 = vandermonde_matrix(x,baselist)
print(A1)



print("\nc)\n")

y = (2,34,7,2.875)

c1 = np.linalg.solve (A1 , y)
print(c1)


def vandermonde_solve(x,*func):
    if len(x)==len(func):
        matrix = []
        for j in range(len(x)):
            matrix_row=[]
            for i in range(len(x)):
                matrix_row.append(func[i](x[j]))
            matrix.append(matrix_row)
        return matrix
    else:
        print("Stützstellenanzahl muss Basisfunktionenanzahl")


A2 = vandermonde_solve((0,2,1,0.5),lambda x:1,lambda x:x,lambda x:x**2,lambda x:x**3)

y = (2,34,7,2.875)

c2 = np.linalg.solve (A2 , y)
print(A2)
print(c2)