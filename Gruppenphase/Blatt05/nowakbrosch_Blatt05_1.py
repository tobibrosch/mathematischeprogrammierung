import csv


print("\na)")

#Zuerst öffnen wir die Datei im Lesemodus
with open("Blatt05_csv_example_input.csv", mode='r') as tab:
    tab_reader = csv.reader(tab)
    
    def line(n):
        """
        Zeilenfunktion
        ----------
        Gibt die n-te Zeile als Liste zurück wobei 1 die erste Zeile ist!

        Parameters
        ----------
        n : Index der gesuchten Zeile

        Returns
        -------
        wanted : Zeile als Liste

        """
        for i in range(n-1):
            next(tab_reader)
        wanted = next(tab_reader)
        return wanted
    header = line(1) # Ist die Kopfzeile für das spätere neuschreiben der Datei
    tab.readline()
    print(line(1))
    
#Innerhalb des Lesemodus starten wir noch den Write Modus
    with open("Blatt05_csv_example_output.csv", mode='w',newline="") as output:
        output_writer = csv.writer(output)
        output_writer.writerow(header+["Gesamtnote"]) 
        for row in tab_reader:        
            grade = 0
            n_count = 0     #zählt wie oft jemand entschuldigt gefehlt hat
            #Bei Unentschuldigtem Fehlen ergibt sich die Gesamtnote zu 6
            if 'u' in row: 
                grade = 6
            #Bei Entschuldigtem Fehlen muss die Anzahl 
            elif 'n' in row:
                for i in range(1,5):
                    if row[i]=='n':
                        n_count += 1
                        if n_count >=2:
                            grade = 0
                            break
                    elif row[i]!='n' and row[i]!='u':
                        grade += float(row[i])
                grade = 1/(len(row)-2)*grade  #len(row)-2 ist Anzahl der Klausuren minus der einen bei der man entschuldigt gefehlt hat
                grade = round(grade,2)
            else:
                grade = 1/(len(row)-1)*sum(float(row[i]) for i in range(1,5)) 
                grade = round(grade,2)
            print(f"{row[0]} hat die Gesamtnote {grade}")
            output_writer.writerow(row+[grade])