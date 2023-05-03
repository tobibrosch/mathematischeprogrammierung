import time
prim=[]
notprim=[]
p=2
n = int(input("Wähle n="))
while p<=n:
    k=1
    if p in notprim:
        p=p+1
        time.sleep(0.01)        
        print(prim,end="\r")
    else:
        p_real=p
        prim.append(p)
        p=p+1
        p_notreal=p_real*2
        notprim.append(p_notreal)
        while p_notreal<n:
            k=k+1
            p_notreal=p_real*k
            notprim.append(p_notreal)        
print(prim)
