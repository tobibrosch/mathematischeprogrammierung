import csv 
import numpy as np
import matplotlib.pyplot as plt

def v(t, r_0=0, v_0=0, g=9.81):
    return r_0 + v_0 * t + 1/2 * g * t**2

with open('text2.csv', mode='w', newline='') as file1:
    writer = csv.writer(file1)
    header = ['Zeit', 'Weg']
    writer.writerow(header)
    def data(n):
        return [[i, v(i)] for i in range(n)]
    
    writer.writerows(data(100))

with open('text2.csv', mode='r', newline='') as file2:
    reader = csv.reader(file2)
    next(reader)  # Überspringe den Header

    def row(n):
        for i in range(n):
            next(reader)
        wanted = next(reader)
        return wanted

    y = [float(row(i)[1]) for i in range(0, 10)]
    x = [i for i in range(0,10)]
    

plt.plot(x, y)
plt.xlabel('Zeit')
plt.ylabel('Weg')
plt.title('Weg-Zeit-Diagramm')
plt.show()
