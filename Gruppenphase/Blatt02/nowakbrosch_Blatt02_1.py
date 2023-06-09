import random
n = random.randint(1,100)
x = float(input("Welche Zahl tippst du?"))
while x!=n:
    if x%1!=0:
        print ("Die Zahl ist keine ganze Zahl zwischen 1 und 100!")
        x = float(input("Möchtest du eine andere Zahl eingeben?"))
    elif x<n:
        print("Leider daneben, deine Zahl ist kleiner gewesen. Rate erneut.")
        x = float(input("Welche Zahl tippst du?"))
    elif x>n:
        print("Leider daneben, deine Zahl ist größer gewesen. Rate erneut.")
        x = float(input("Welche Zahl tippst du?"))
print("Richtig die gesuchte Zahl ist", n)
