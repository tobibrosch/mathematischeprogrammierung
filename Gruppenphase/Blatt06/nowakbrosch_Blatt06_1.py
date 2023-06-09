import numpy as np
import matplotlib.pyplot as plt

#Aufgabe 1

#a

A = np.array([[1,2,1],[-1,2,-3],[0,1,-2]])

def frobenius_norm(A):
    return np.sqrt(np.sum(A*A))

print("a.)",frobenius_norm(A))

#b 
def info(A):
    return (np.min(A),np.mean(A),np.max(A))

print("b.)",info(A))

#c
def maximum_norm(A):
    return np.max(np.sum(np.abs(A), axis=1))

print("c.)",maximum_norm(A))

#d
def upper3(d,u1,u2,N):
    if N>=2:
        return d*np.eye(N)+u1*np.eye(N,N,1)+u2*np.eye(N,N,2)
    else:
        print("Die Dimension muss mindestens 2 sein")
        
print("d.)",upper3(1,2,3,7))

#e
def insert(B, start_row, start_col, A):
    M, N = B.shape
    I, J = A.shape

    #Überprüfung ob die Matrix B die richtige Dimension hat
    if not(M <= I - start_row and N <= J - start_col):
        print("Die Dimension von B ist nicht gültig")

    A[start_row:start_row+M, start_col:start_col+N] = B
    return A

B = np.array([[1, 0],
              [0, 3],
              [0, 1]])

A = np.ones((5,5))
start_row = 1
start_col = 3

result = insert(B, start_row, start_col, A)
print("e.)",result)