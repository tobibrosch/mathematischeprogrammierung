d1 = [9, 0, 7, 4, 5, 2, 3, 8, 1, 3, 6, 5]
d2=  [9, 0, 7, 4, 5, 2, 3, 8, 1, 3, 6, 5]

print(d1)
print("")
print(d2)
print("")
print("")
d1[d2.index(min(d2))], d1[0] = d1[0], d1[d2.index(min(d2))]
d2[d2.index(min(d2))], d2[0] = d2[0], d2[d2.index(min(d2))]
d2.remove(d2[0])
print(d1)
print("")
print(d2)
print("")
print("")
d1[d2.index(min(d2))+1], d1[1] = d1[1], d1[d2.index(min(d2))+1]
d2[d2.index(min(d2))], d2[0] = d2[0], d2[d2.index(min(d2))]
d2.remove(d2[0])
print(d1)
print("")
print(d2)
print("")
print("")
d1[d2.index(min(d2))+2], d1[2] = d1[2], d1[d2.index(min(d2))+2]
d2[d2.index(min(d2))], d2[0] = d2[0], d2[d2.index(min(d2))]
d2.remove(d2[0])
print(d1)
print("")
print(d2)
print("")
print("")
d1[d2.index(min(d2))+3], d1[3] = d1[3], d1[d2.index(min(d2))+3]
d2[d2.index(min(d2))], d2[0] = d2[0], d2[d2.index(min(d2))]
d2.remove(d2[0])
print(d1)
print("")
print(d2)
print("")
print("")