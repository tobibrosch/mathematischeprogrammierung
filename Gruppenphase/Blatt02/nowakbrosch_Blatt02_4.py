import time
clear = '\033[2J'

n= int(input("Wähle n= "))
if n==1:
    print("Liste ist leer [] da 1 keine Primzahl")
else:
    unsort = list(range(2,n+1))
    z=0
    p_real=unsort[z]
    while p_real**2<n:
        k=2
        p_notreal=p_real*k
        print(unsort,end="\r")
        print(end=clear)
        time.sleep(2.)
        while p_notreal<=n:
            if p_notreal in unsort:
                unsort.remove(p_notreal)
                #print("Schleife 2 entfernt",p_notreal," und es wird ",unsort)
                k=k+1
                p_notreal=p_real*k
            else:
                k=k+1
                p_notreal=p_real*k
        z=z+1  
        #print("Schleife 1 zeigt Liste ohne Vielfache von",p_real,unsort)  
        p_real=unsort[z]
    print(unsort)