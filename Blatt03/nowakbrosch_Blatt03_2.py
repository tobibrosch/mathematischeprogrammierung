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


#a

gedicht_kb = []
kleinbuchstaben = ('abcdefghijklmnopqrstuvwxyzäöüß')
grossbuchstaben = ('ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ')


for i in str(text):
    if i in kleinbuchstaben:
        gedicht_kb.append(i)
    if i in grossbuchstaben:
        i = kleinbuchstaben[int(grossbuchstaben.index(i))]
        gedicht_kb.append(i)
    
#print("".join(gedicht_kb))

#b

buchstaben = ('abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ')

liste_bs = [i for i in buchstaben if i in text]
liste_anz = [text.count(i) for i in buchstaben if i in text]


haeufig_anz = max(liste_anz)
hauefig_bs = liste_bs[liste_anz.index(haeufig_anz)]

        
#print(f"Der am häufigsten vorkommende Buchstabe ist {hauefig_bs}, er kommt {haeufig_anz}-mal in dem Text vor.")


buchstaben = ('abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ')

bs_anz = {text.count(i):i for i in buchstaben if i in text}

max_anz = max(text.count(i) for i in buchstaben if i in text)

print(f"Der am häufigsten vorkommente Buchstabe ist {bs_anz[max_anz]}, er kommt {max_anz}-mal in dem Text vor.")





















