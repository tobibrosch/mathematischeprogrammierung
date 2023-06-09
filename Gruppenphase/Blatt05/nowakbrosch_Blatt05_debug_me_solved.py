"""

Ein Programm, dass leider nicht funktioniert.

Korrigieren Sie die 7 Fehler und schreiben Sie als Kommentar den Fehlertyp
dazu (Syntaxfehler, Laufzeitfehler, logischer Fehler)

"""

def flip_lr (my_list):
    """
    Diese Funktion soll eine Liste umdrehen.
    """

    length = len(my_list)-1                          
    ##1. Syntaxfehler: Die Indizierung einer Liste beginnt bei 0 und geht bis len(list)-1 demnach sollte i nicht bis len(list) laufen)
    
    # Die umgedrehte Liste
    flipped_list = [None]*length
    
    for i in range(length):                          ##2. Syntaxfehler: Hier hat ein Doppelpunkt gefehlt um die for-Schleife einzuleiten
        flipped_list[i] = my_list[length-i]
     
    return my_list


def find_smallest_entry (my_list):
    """
    Diese Funktion soll den kleinsten Eintrag der Liste finden.
    """
    
    length = len(my_list)
    
    # Index des kleinsten Eintrags
    i_min = 0
    
    for i in range(length):                     
        if (my_list[i_min] > my_list[i]):           ##3.Logischer Fehler: < muss zu > werde, da sonst der größte Eintrag gefunden wird
            i_min = i
    
    return my_list[i_min]                           ##4.Logischer Fehler: Funktion soll kleinsten Eintrag und nicht Index des kleinsten Eintrags finden


def transpose(my_list_of_lists):
    """
    Diese Funktion gibt das transponierte Äquivalent zurück
    """
    number_of_lines   = len(my_list_of_lists)
    number_of_columns = len(my_list_of_lists[0])
    # Die transponierte Liste
    transposed_list_of_lists = [[0]*number_of_lines for k in range(number_of_columns)]      
    ##5. Logischer Fehler: Damit die Einträge der Listen die richtige Anzahl haben müssen hier columns und lines vertauscht werden
    ##6. Logischer Fehler: durch *number_of_columns wird mehrfach auf die Innere Liste zugegriffen und nicht jede innere Liste seperat gespeichert
    ##                     das kann zum Beispiel durch eine for-Schleife oder durch eine List Comprehension behoben werden
    # Befüllen der Einträge
    for i in range(number_of_lines):
      for j in range(number_of_columns):
        transposed_list_of_lists[j][i] = my_list_of_lists[i][j]
    return transposed_list_of_lists



# Wir testen die ersten beiden Funktionen mit einer Besipielliste
list_1 = [5,4,3,2,1,0]
print("Wenn wir die Liste ", list_1,
      " umdrehen, erhalten wir ", flip_lr(list_1))   ##7. Syntaxfehler: Die Funktion zum umdrehen einer Liste wurde als flip_lr und nicht flip_rl eingeführt
print("Der kleinste Eintrag der Liste ", list_1,
      " ist ", find_smallest_entry(list_1))
print()

# Wir testen mit einer weiteren Beispielliste
list_2 = [2,1,2,1,2,1,2]
print("Wenn wir die Liste ", list_2,
      " umdrehen, erhalten wir ", flip_lr(list_2))
print("Der kleinste Eintrag der Liste ", list_2,
      " ist ", find_smallest_entry(list_2))
print()

# Wir testen das Transponieren mit transpose mit einer Besipielliste
list_of_lists = [[1,1],[2,2]]
print("Wenn wir ", list_of_lists,
      "transponieren, erhalten wir", transpose(list_of_lists))
print()

# Wir testen mit einer weiteren Beispielliste
list_of_lists = [[1,0],[0,1],[2,2]]
print("Wenn wir ", list_of_lists,
      "transponieren, erhalten wir", transpose(list_of_lists))
