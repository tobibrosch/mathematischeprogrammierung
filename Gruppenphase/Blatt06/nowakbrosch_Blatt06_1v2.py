from math import cos, tan , pi
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
v = float(input("Abwurfgeschwindigkeit: "))
while v<=0:
    v = float(input("Abwurfgeschwindigkeit: "))
    if v>0:
        break

phi_g = float(input("Abwurfwinkel: "))
while phi_g<=0 or phi_g>=90:
    phi_g = float(input("Abwurfwinkel: "))
    if phi_g>0 and phi_g<90:
        break
phi_b = phi_g * pi / 180

x = np.linspace(0, 10, num=100)
f = x * tan(phi_b) - (g * x**2) / (2 * v**2 * (cos(phi_g))**2)
plt.plot(x, f)
plt.xlabel('Flugweite')
plt.ylabel('Flughöhe')
plt.ylim(0,np.max(f)+0.1)
plt.title('Flüghöhe je nach Flugweite')
plt.show()


