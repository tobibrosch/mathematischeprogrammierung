from math import sqrt
from math import acos

def vnorm(v):
    """ 
    Euklidische Norm
    ---------------------
    Berechnung der Euklideschen Norm eines n-Dimensionalen Vektors in R
    ---------------------
    Parameter:
        v = Eingabe eines tupels mit größe n
        sum = 0 ist die Summe der Diskriminate
    ---------------------
    For Schleife Berechnet die Summe der Quadrate der Einträge unter der Diskriminate

    sqrt(sum) berechnet die Quadratwurzel der berechneten Summe "sum" und gibt dies als Wert der Funktion zurück
    """
    y = 0
    for i in v: 
        y+=i**2
    z = sqrt(y)
    return z

def vsum(*vectors):
    """
    Addition Vektoren
    -------------------
    Summiert endlich viele dreidimensionale Vektoren
    -------------------
    Parameter: 
        vectors = Einhabe von einem tupel mit drei Elementen 
    
    Gibt ein tupel mit 3 Elementen zurück

    """
    x = 0
    y = 0
    z = 0
    for i in vectors:
        x = x + i[0]
        y = y + i[1]
        z = z + i[2]
    v = (x,y,z)
    return v


def vdotproduct(v1,v2):
    """
    Skalarprodukt
    ---------------
    Berechnet das Skalarprodukt zweier n-Dimensionaler Vekoren aus R
    ---------------
    Parameter: 
        v1 = Vektor 1 als Tupel mit n Elementen 
        v2 = Vektor 2 als Tupel mit n Elementen
    Output: 
    """
    v = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    return v

def vangle(v1,v2):
    """
    Winkelberechnung
    -------------------
    Berechnet den Winkel zwischen zwei 3-dimensionalen Vektoren
    -------------------
    Parameter:
        v1= Tupel mit 3 Elemeten 
        v2= Tupel mit 3 Elemeten 
    Benutz acos für arus cosinus
    Benutz die davor definierten funktionen vdotproduct und vnorm
    Abfrage aufgrund der Machinenungenauigkeit mit einer tolaranz damit ein Rechter Winkel erkannt wird!
    Toleranz liegt bei 0.00001
    --------------------
    Output: 
        Winkel in Rad mit type float
    """
    teta = acos(vdotproduct(v1,v2) / (vnorm(v1)*vnorm(v2)))
    return teta