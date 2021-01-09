import time
from generating_numbers import *
import random


def swap(L, left, right):
    """Zamiana miejscami dwóch elementów na liście."""
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item
    
def insertsort(L, left, right):
    if left < right:
        insertsort(L, left, right-1)
        item = L[right]
        j = right
        # Tu widać, że wartownik upraszcza warunek pętli.
        while j > left and item < L[j-1]:   # robimy miejsce na item
            L[j] = L[j-1]
            j = j-1
        L[j] = item

def shakersort(L, left, right):
    k = right
    while left < right:
        for j in range(right, left, -1):   # od prawej
            if L[j-1] > L[j]:
                swap(L, j-1, j)
                k = j
        left = k
        for j in range(left, right):   # od lewej
            if L[j] > L[j+1]:
                swap(L, j, j+1)
                k = j
        right = k

def bubblesort(L, left, right):
    limit = right
    while True:
        k = left-1   # lewy wskaźnik przestawianej pary
        for i in range(left, limit):
            if L[i] > L[i+1]:
                swap(L, i, i+1)
                k = i
        if k > left:
            limit = k
        else:
            break
        
def selectsort(L, left, right):
    for i in range(left, right):
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item

#funkcja mierząca czas wykonania funkcji, którą przyjmuje za swój argument
def measure(funct, L, N):
    start_time = time.perf_counter()
    funct(L, 0, N-1)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time

N=10
#Co robi kod poniżej:
#Zachodzi wywoływanie wszystkich funkcji sortujacych dla listy zawierającej 10**2, 10**3, 10**4, 10**5, 10**6 losowych liczb całkowitych.
#Budowany jest słownik dla każdego przebiegu pętli (dla każdej długości listy). W słowniku kluczem jest czas wykonania sortowania przez daną funkcję,
#a wartością jest nazwa tej funkcji. Każdy słownik jest posortowany według klucza (czyli według czasu wykonania sortowania przez daną funkcję)
#po to, by móc porównać czasy, w jakich te funkcje wykonały sortowania list
for i in range(2, 7):
    times = {}
    L= random_integers(N**i)
    a = measure(bubblesort, L, N)
    times[a] = bubblesort.__name__
    b = measure(insertsort, L, N)
    times[b] = insertsort.__name__
    c = measure(shakersort, L, N)
    times[c] = shakersort.__name__
    d = measure(selectsort, L, N)
    times[d] = selectsort.__name__
    print("For list of length ", N**i, "the times of execution of sorting functions are: ")
    for key in sorted(times.keys()) :
        print(key , " :: " , times[key])



    

