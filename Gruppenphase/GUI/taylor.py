from sympy import symbols, diff, log, factorial as fac, sin, exp, tan
import numpy as np
import matplotlib.pyplot as plt
# Symbole definieren
x = symbols('x')

# Funktion definieren
f = sin(x)*x

# Taylorreihe berechnen
def Taylor(f, n, a):
    taylor_sum = 0
    for i in range(n+1):
        taylor_sum += diff(f, x, i).subs(x, a) / fac(i) * (x - a) ** i
    return taylor_sum

x_values = np.linspace(-10,10,num=200)
k=0
# Schleife zum Aktualisieren des Plots
for i in range(0,30):
    
    # Lösche den vorherigen Plot
    if k%5==0:
        plt.clf()
    k+=1
    # Plot neu erstellen
    plt.plot(x_values,[f.subs(x,i)for i in x_values])
    plt.plot(x_values, [Taylor(f,i,0).subs(x,j) for j in x_values])
    plt.ylim(-10,10)
    # Zeige den aktualisierten Plot an
    plt.draw()

    # Füge hier optional eine Pause ein, um die Änderungen zu sehen
    plt.pause(1)

# Zeige den endgültigen Plot an
#plt.ylim(-2,2)
plt.show()
