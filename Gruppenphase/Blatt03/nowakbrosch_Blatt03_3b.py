import random
import time

def selectsort(list):
    print("Selectionsort algorithm:")
    start = time.perf_counter()
    for n in range(0, len(list) - 1):
       	ix_min = n
        for s in range(n + 1, len(list)):
       		if list[s] < list[ix_min]:
       			ix_min = s
       	list[n], list[ix_min] = list[ix_min], list[n]
    end = time.perf_counter()
    print(f"Die Durchlaufzeit betrug: {end-start}")

def bubblesort(list):
    swapped = True
    print("Bubblesort algorithm:")
    # Solange wir noch Elemente tauschen müssen, sind wir noch
    # nicht fertig
    start = time.perf_counter()
    while swapped:
        swapped = False # optimistische Annahme: im Folgenden wird nichts getauscht
        # Laufe durch die Liste und tausche benachbarte Elemente,
        # wenn das spätere Element kleiner ist als das vorherige.
        for i in range(1, len(list)):
            if list[i-1] > list[i]:
                # Tauschen der benachbarten Elemente:
                list[i], list[i-1] = list[i-1], list[i]  # Erinnerung: das sind zwei simultane Zuweisungen
                swapped = True
    end = time.perf_counter()
    print(f"Die Durchlaufzeit betrug: {end-start}")


def pysort1(list):
    print("list.sort() algorithm:")
    start = time.perf_counter()
    list.sort()
    end = time.perf_counter()
    print(f"Die Durchlaufzeit betrug: {end-start}")

    
def pysort2(list):
    print("sorted() algorithm:")
    start = time.perf_counter()
    list = sorted(list)
    end = time.perf_counter()
    
    print(f"Die Durchlaufzeit betrug: {end-start}")


pseudolist = [random.randint(0,100001)*0.00001 for i in range(0,100000)]

print("Die Durchlaufzeiten betragen:")

selectsort(pseudolist)
bubblesort(pseudolist)
pysort1(pseudolist)
pysort2(pseudolist)

