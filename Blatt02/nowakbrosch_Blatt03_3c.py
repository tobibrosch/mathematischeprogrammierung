d1= [9, 0, 7, 4, 5, 2, 3, 8, 1, 3, 6, 5]
for k in range(len(d1)):
    min = k
    for i in range(k + 1, len(d1)):
        if d1[i] < d1[min]:
            min = i
    (d1[k], d1[min]) = (d1[min], d1[k])
print(d1)