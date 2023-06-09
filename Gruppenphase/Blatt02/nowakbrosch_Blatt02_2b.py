import math
x=2
for i in range(1,16):
    h=10**(-i)
    sin_dx=(math.sin(x+h)-math.sin(x))/h
    e_x=abs(math.cos(x)-sin_dx)
    print(f"Für {h} ist der Fehler bei={e_x}")

#Der Fehler steigt für kleine h, weil wir für sin_dx mit floats rechnen.
#Die Genauigkeit der Floats ist durch die Maschinengenauigkeit begrenzt.