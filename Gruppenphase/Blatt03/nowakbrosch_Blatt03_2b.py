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


buchstaben = ('abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ')

liste_bs = [i for i in buchstaben if i in text]
liste_anz = [text.count(i) for i in buchstaben if i in text]
zaehlen = dict(zip(liste_bs,liste_anz))

print(f"In folgendem Verzeichnis wird die Häufigkeit der einzelnen Buchstaben gezählt:" )
print(zaehlen)

haeufig_anz = max(liste_anz)
hauefig_bs = liste_bs[liste_anz.index(haeufig_anz)]

        
print(f"Der am häufigsten vorkommende Buchstabe ist {hauefig_bs}, er kommt {haeufig_anz}-mal in dem Text vor.")

