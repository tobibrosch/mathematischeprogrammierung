import matplotlib.pyplot as plt
import numpy as np

# Daten für den Plot
alpha = np.linspace(-10,10,num=10)
x = np.linspace(-10, 10, num=1000)
def y(i):
    return np.sin(x*i)

# Erstelle die Figure und die Axes

k=0
# Schleife zum Aktualisieren des Plots
for i in alpha:
    
    # Lösche den vorherigen Plot
    if k%5==0:
        plt.clf()
    k+=1
    # Plot neu erstellen
    plt.plot(x, y(i))

    # Zeige den aktualisierten Plot an
    plt.draw()

    # Füge hier optional eine Pause ein, um die Änderungen zu sehen
    plt.pause(1)

# Zeige den endgültigen Plot an
plt.show()
