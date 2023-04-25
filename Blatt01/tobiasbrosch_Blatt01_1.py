length = 20
progress = 11
i=0
while i<20:
    i=i+1
    print("Vorgang läuft...")
    progress_bar = "[" + "="*i + ">" + " "*(length-i) + "]"
    print(progress_bar)
