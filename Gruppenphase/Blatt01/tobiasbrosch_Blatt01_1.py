import time

length = 20
progress = 11
i=0
print("Vorgang läuft...")
while i<20:
    i=i+1
    time.sleep(0.05)
    progress_bar = "[" + "="*i + ">" + " "*(length-i) + "]"
    print(progress_bar,end="\r") 
print("["+"="*(i+1)+"]")