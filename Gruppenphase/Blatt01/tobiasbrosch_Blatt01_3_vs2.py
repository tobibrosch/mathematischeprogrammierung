
n = int(input("Wähle Dachgröße="))
n=n-1
if n==0:
    print("/\\")
    print("||")
elif n>=1:
    x=n
    p=x
    while x >= 1:
        dach= " "*x + "/" + " "*(p-x)*2 + "\\"
        x=x-1
        print(dach)

    x= p*2
    unterdach= "/" + "_"*x + "\\"
    print(unterdach)

    x=n
    while x >= 1:
        body="|" + " "*(p-x) + "\\" + " "*(x-1)*2 + "/" + " "*(p-x) + "|"
        x=x-1
        print(body)
    x=n
    while x >= 2:
        body="|" + " "*(x-1) + "/" + " "*(p-x)*2 + "\\" + " "*(x-1) + "|"
        x=x-1
        print(body)
    x=n*2
    boden= "|/" + "_"*(x-2) + "\\|"
    print(boden)
else:
    print("Dachgröße muss größer gleich 1 sein!")