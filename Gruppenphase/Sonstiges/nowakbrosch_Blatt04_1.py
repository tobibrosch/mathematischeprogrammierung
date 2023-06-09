v = (3,4,-1)
from math import sqrt
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
    sum=0
    for i in range(len(v)):
        sum = sum + v[i]**2
    return sqrt(sum)

print(vnorm(v))

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
    a=0
    b=0
    c=0
    for i in range(len(vectors)):
        a = a+ vectors[i][0]
        b = b+ vectors[i][1]
        c = c+ vectors[i][2]
    return (a,b,c)


print(vnorm(vsum((1,2,3),(1,2,3),(2,3,-2))))

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

    sum=0
    if len(v1)==len(v2):
        for i in range(len(v1)):
            sum= sum + v1[i]*v2[i]
        return sum 
    return "Die Vektoren müssen gleicher Dimension sein!"
print(vdotproduct((1,2,3),(1,2,3)))

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
    rechterwinkel = acos(vdotproduct(v1,v2)/(vnorm(v1)*vnorm(v2)))
    if rechterwinkel < 0.000001:
        return 0
    else:
        return acos(vdotproduct(v1,v2)/(vnorm(v1)*vnorm(v2)))
print(vangle((0,0,1),(1,0,0)))


