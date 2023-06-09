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




gedicht_kb = []
kleinbuchstaben = ('abcdefghijklmnopqrstuvwxyzäöüß')
grossbuchstaben = ('ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ')


for i in text:
    if i in kleinbuchstaben:
        gedicht_kb.append(i)
    if i in grossbuchstaben:
        i = kleinbuchstaben[int(grossbuchstaben.index(i))]
        gedicht_kb.append(i)
print("".join(gedicht_kb))

