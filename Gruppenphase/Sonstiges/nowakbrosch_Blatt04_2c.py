import numpy as np

print("\nc)\n")

#Hier wird die Basisfunktionenliste angegeben
baselist = [lambda x : 1, lambda x : x,lambda x : x**2,lambda x : x**3]  
#Hier werden die Stützstellen als Tupel angegeben
x = (0,2,1,0.5)
#Hier werden die Funktionswerte angegeben
y = (2, 34, 7, 2.875)

def vandermonde_solve(x,y,baselist):
    matrix = []
    for j in range(len(x)):
        matrix_row=[]
        for i in range(len(x)):
            matrix_row.append(baselist[i](x[j]))
        matrix.append(matrix_row)
    return np.linalg.solve (matrix, y)

c = vandermonde_solve(x,y,baselist)
print(c)

print("\nd)\n")

#Hier wird die Basisfunktionenliste angegeben
baselist = [lambda x : 1, lambda x : x,lambda x : x**2,lambda x : x**3]  
#Hier werden die Stützstellen als Tupel angegeben
x = (0,2,1,0.5)
#Hier werden die Funktionswerte angegeben
y = (2, 34, 7, 2.875)
#Hier wird der grad angegeben

def vandermonde_solve(x,y,g,baselist):
    matrix = []
    for j in range(g):
        matrix_row=[]
        for i in range(g):
            matrix_row.append(baselist[i](x[j]))
        matrix.append(matrix_row)
    return np.linalg.solve (matrix, y[0:g])

#g-1 gibt den Grad an und läuft deshalb hier von 0 bis 3
for g in range(1,5):
    c1 = vandermonde_solve(x,y,g,baselist)
    print(f"{c1}")

