data = [9,0,7,4,5,2,3,8,1,3,6,5]
data_sort=[]
while len(data)>0:
    data_sort.append(min(data))
    data.remove(min(data))
    print(data_sort)
    


