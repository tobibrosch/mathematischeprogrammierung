import vector_calculus as vec
import random
import math
import sys

v1 = (0,0,3)
v2 = (1,0,0)

print("a)")
print(vec.vnorm(v1))

print("\nb)")
print(vec.vsum(v1,v2))

print("\nc)")
print(vec.vdotproduct(v1,v2))

print("\nd)")
print(vec.vangle(v1,v2))


rand_vec = []

for i in range (10):
    vecs = (((random.random())*20000)-10000, ((random.random())*20000)-10000, ((random.random())*20000)-10000)
    rand_vec.append(vecs)

#rand_vecs ist Liste mit 100 beliebigen Vektoren mit Einträgen zwischen -10000 und 10000


#Betrag größer gleich null für 100 bliebigen Vektoren
for i in rand_vec:
    if vec.vnorm(i) <0:
        print("Hilfe der Betrag ist negativ")    


    
#

for i in rand_vec:
    if math.fabs(vec.vnorm(i)**2-vec.vdotproduct(i,i)) > \
    max(math.fabs(vec.vnorm(i)**2), math.fabs(vec.vdotproduct(i,i)))*sys.float_info.epsilon:
        print("Hilfe die Gleichung stimmt nicht!")

#
for v in rand_vec:
    for w in rand_vec:
        for x in rand_vec:
            if math.fabs((vec.vdotproduct(vec.vsum(v,w),x))-((vec.vdotproduct(v,x))+(vec.vdotproduct(w,x))))> 0.0000001:
                print("Hilfe die Gleichung gilt nicht!")


#Weitere sinnvolle Eigenschaft: <v,w> = <w,v>
for x in rand_vec:
    for w in rand_vec:
        if math.fabs(vec.vdotproduct(x,w)-vec.vdotproduct(w,x)) > \
        max(math.fabs(vec.vdotproduct(x,w)),math.fabs(vec.vdotproduct(w,x)))*sys.float_info.epsilon:
            print("Hilfe die Gleichung stimmt nicht!")             


#Noch eine weitere sinnvolle Eigenschaft: <v,w> > ||v||*||w||

for v in rand_vec:
    for w in rand_vec:
        if vec.vdotproduct(v,w) - vec.vnorm(v)*vec.vnorm(w)>= max(math.fabs(vec.vdotproduct(v,w)),vec.vnorm(v)*vec.vnorm(w))*sys.float_info.epsilon:
            print("Hilfe die Gleichung gilt nicht!")


