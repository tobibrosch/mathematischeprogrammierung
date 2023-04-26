d1 = [9,0,7,4,5,2,3,8,1,3,6,5]
d2 = [9,0,7,4,5,2,3,8,1,3,6,5]

for i in range(len(d1)):
    d1[d2.index(min(d2))+i], d1[i] = d1[i], d1[d2.index(min(d2))+i]
    d2[d2.index(min(d2))], d2[0] = d2[0], d2[d2.index(min(d2))]
    d2.remove(d2[0])
print(d1)
