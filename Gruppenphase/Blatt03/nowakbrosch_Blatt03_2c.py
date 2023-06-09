# "Er ist’s" von Eduard Mörike

text = """Frühling läßt sein blaues Band
Wieder flattern durch die Lüfte
Süße, wohlbekannte Düfte
Streifen ahnungsvoll das Land
Veilchen träumen schon,
Wollen balde kommen
Horch, von fern ein leiser Harfenton!
Frühling, ja du bist’s!
Dich hab ich vernommen!"""

kleinbuchstaben = ('abcdefghijklmnopqrstuvwxyzäöüß')
grossbuchstaben = ('ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ')


#a
text = text.replace("\n"," ")
text = text.replace(",","")
text = text.replace("!","")
#print(text)

text = text.split(" ")

print(text)

worte = [i for i in text]
worte_anz = [text.count(i) for i in text]

dict_wort = dict(zip(worte,worte_anz))

print(dict_wort)

max_anz = {max(worte_anz)}

for i in max_anz:
    print(f"Das Wort das am häufigsten vorkommt ist: {worte[worte_anz.index(i)]} es kommt {i}-mal vor")