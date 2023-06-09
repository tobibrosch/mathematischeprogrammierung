"""
Modul zur Vektorrechnung.

Dieses Modul ermöglicht 3-dimensionale Vektorrechnung.
"""

from math import sqrt, acos

def vsum(*vectors):
    """
    Berechnung der Summe der 3-dimensionalen Vektoren v1 und v2

    """
    for vec in vectors:
        assert len(vec) ==3, "Die Vektorenbrauchen genau 3 Einträge!"
        assert type(vec)==tuple, "Die Vektoren sollen als Tupel eingegeben werde"
        for i in range(3):
            assert type(vec[i])==int or type(vec[i])==float, "Keine Zahlen als Einträge in den Vektoren" 
    return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]), sum([v[2] for v in vectors]))


def vdotproduct(v1,v2):
    """
    Berechnung des Skalarprodukts der 3-dimensionalen Vektoren v1 und v2
    """
    assert len(v1) ==3 and len(v2)==3, "Die Vektorenbrauchen genau 3 Einträge!"
    assert type(v1)==tuple and type(v2)==tuple  , "Die Vektoren sollen als Tupel eingegeben werde"
    for i in range(3):
        assert type(v1[i])==int or type(v1[i])==float, "Keine Zahlen als Einträge in den Vektoren" 
        assert type(v2[i])==int or type(v2[i])==float, "Keine Zahlen als Einträge in den Vektoren"     
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def vnorm(vector):
    """
    Berechnung der (euklidischen) Norm des 3-dimensionalen Vektors vector
    """
    assert len(vector) ==3, "Die Vektorenbrauchen genau 3 Einträge!"
    assert type(vector)==tuple, "Die Vektoren sollen als Tupel eingegeben werde"
    for i in range(3):
        assert type(vector[i])==int or type(vector[i])==float, "Keine Zahlen als Einträge in den Vektoren" 
            
    return sqrt(vdotproduct(vector, vector))

def vcrossproduct(v1, v2):
    """
    Berechnung des Kreuzprodukts der 3-dimensionalen Vektoren v1 und v2
    """
    assert len(v1) ==3 and len(v2)==3, "Die Vektorenbrauchen genau 3 Einträge!"
    assert type(v1)==tuple and type(v2)==tuple  , "Die Vektoren sollen als Tupel eingegeben werde"
    for i in range(3):
        assert type(v1[i])==int or type(v1[i])==float, "Keine Zahlen als Einträge in den Vektoren" 
        assert type(v2[i])==int or type(v2[i])==float, "Keine Zahlen als Einträge in den Vektoren" 
    
    return (
        v1[1]*v2[2]-v1[2]*v2[1], 
        v1[2]*v2[0]-v1[0]*v2[2],
        v1[0]*v2[1]-v1[1]*v2[0],
    )

def vangle(v1, v2):
    """
    Berechnung des Winkels zwischen den 3-dimensionalen Vektoren v1 und v2
    """
    assert len(v1) ==3 and len(v2)==3, "Die Vektorenbrauchen genau 3 Einträge!"
    assert type(v1)==tuple and type(v2)==tuple  , "Die Vektoren sollen als Tupel eingegeben werde"
    for i in range(3):
        assert type(v1[i])==int or type(v1[i])==float, "Keine Zahlen als Einträge in den Vektoren" 
        assert type(v2[i])==int or type(v2[i])==float, "Keine Zahlen als Einträge in den Vektoren" 
    
    assert vnorm(v1)!=0 and vnorm(v2)!=0, "Norm der Vektoren darf nicht null sein, weil sonst für die Berechnung durch 0 geteilt wird"
    return acos(vdotproduct(v1, v2) / vnorm(v1) / vnorm(v2))


print(vcrossproduct((7,0,1.1),(0,0,0,9)))