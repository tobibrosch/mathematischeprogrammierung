data = [9, 0, 7, 4, 5, 2, 3, 8, 1, 3, 6, 5]
data_min = [9, 0, 7, 4, 5, 2, 3, 8, 1, 3, 6, 5]

for i in range (len(data)):
    data[data_min.index(min(data_min))+i], data[i] = data[i], data[data_min.index(min(data_min))+i]
    data_min[data_min.index(min(data_min))], data_min[0] = data_min[0], data_min[data_min.index(min(data_min))]
    data_min.remove(data_min[0])
print(data)
print(data_min)


