data = [9,0,7,4,5,2,3,8,1,3,6,5]

print("Vor der Sortierung gilt:")
print (f"Die Liste data sieht wiefolgt aus: {data}")
print(f"Die d dieser Liste lautet: {id(data)} \n") 

print("Nach der Sortierung mit sorted(list) gilt:")
data_new1 = sorted(data)
print(f"Die Liste sorted(data) sieht wiefolgt aus: {data_new1}")
print(f"Und hat folgende Id: {id(data_new1)} ")
print(f"Während die ursprüngliche Liste nun so aussieht: {data}")
print(f"Und folgende Id besitzt: {id(data)} \n")

print("Nach der Sortierung mit list.sort() hingegen gilt:")
data_new = data.sort()
print(f"Die neue Liste sind wie folgt aus: {data_new}")
print(f"Und besitzt folgenge Id: {id(data_new)}")
print(f"Während die ursprüngliche Liste nun so aussieht: {data}")
print(f"Und folgende Id besitzt: {id(data)}")

# sorted(list) erzeugt also eine neue Liste und ändert an der ursprünglichen Liste nichts
# list.sort() hingegen sortiert nur die ursprüngliche Liste 
# und ist selbst keine neue Liste und referenziert auch nicht auf die ursprüngliche Listeh