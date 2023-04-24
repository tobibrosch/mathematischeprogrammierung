import random
n=random.randint(1,100)
x = float(input("Welche Zahl tippst du?"))
while x!=n:
    if x<n:
        print("Leider daneben, deine Zahl ist kleiner gewesen. Rate erneut.")
        x = float(input("Welche Zahl tippst du?"))
    elif x>n:
        print("Leider daneben, deine Zahl ist größer gewesen. Rate erneut.")
        x = float(input("Welche Zahl tippst du?"))
print("Richtig die gesuchte Zahl ist", n)
