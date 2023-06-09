import numpy as np
import matplotlib.pyplot as plt

#a)
data = np.loadtxt('Blatt06_sunspot_2000.csv',delimiter=',', skiprows=1)

decimal_date = data[:, 3]       # Dezimales Datum
sunspots = data[:, 4]           # Anzahl der Sonnenflecken


#b) Berechnung der Mittelwerte

mittelwerte_d = decimal_date[100:len(decimal_date)-99]
x = np.arange(100,len(decimal_date)-99)
mittelwerte_f = [1/201*np.sum(sunspots[x-100:x+101]) for x in x]

#c)

plt.subplot(2, 1, 1)
plt.title("Sonnenfleckendiagramme")
plt.plot(x,sunspots[x],label='Rohdaten')
plt.plot(x,mittelwerte_f, label='Mittelwerte')
plt.xlabel(f"Tage ab dem Dezimaldatum {decimal_date[100]}")
plt.ylabel("Anzahl der Sonnenflecken")
plt.legend()
plt.show()


plt.subplot(2, 1, 2)
plt.legend()
plt.xlabel("Anzahl der Sonnenflecken")
plt.ylabel("Anzahl der Tage")

bins = 15


# wir sehen, dass wir wenig sehen, deshalb nochmal hübscher
plt.hist(sunspots,bins,rwidth=0.9)
plt.show()
