
n = int(input("Wähle Pascaldreieckstufe n="))
if n==1: 
    pascal=[1,1]
    print(pascal)
elif n==0:
    pascal=[1]
    print(pascal)
elif n>1:
    pascal_bevor=[1,1]
    for k in range(n-1):
        pascal=[]
        pascal.append(pascal_bevor[0])
        i=0
        while i < k+1:
            pascal.append(pascal_bevor[i]+pascal_bevor[i+1])
            i=i+1
        pascal.append(pascal_bevor[i])
        pascal_bevor= list.copy(pascal)
        print(pascal)
else:
    print("Die Zahl muss größer gleich 0 sein")

