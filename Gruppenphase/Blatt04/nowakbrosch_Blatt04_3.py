import datetime as dt

print("\na\n")

v1 = dt.datetime(day=8,month=5,year=2023)
#Funktioniert weil Default bei time auf 00:00 
v2 = dt.datetime(2023,5,15,15,0)

print(v1)
print(v2)

print("\nb)\n")

v3=abs(v1-v2)
print(v3)

print("\nc)\n")

print(v3.total_seconds())

print("\nd)\n")

v4 = v1 - dt.timedelta(hours=1, minutes=30)
v5 = v2 - dt.timedelta(hours=1, minutes=30)

print(v4)
print(v5)