d1 = [9,0,7,4,5,2,3,8,1,3,6,5]
d2 = list.copy(d1)
import time
for i in range(len(d1)):
    d1[d2.index(min(d2))+i], d1[i] = d1[i], d1[d2.index(min(d2))+i]
    d2[d2.index(min(d2))], d2[0] = d2[0], d2[d2.index(min(d2))]
    d2.remove(min(d2))
    time.sleep(2-0.1*i)
    if i<len(d1)-2:
        print(d1,"\r")
        print(d2,"\r")
    else:
        break 
print(d1)
