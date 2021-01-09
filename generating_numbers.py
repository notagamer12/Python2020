import random

def nIntegers(N):
    integers = list(range(N))
    return integers

def random_integers(N):
    integers = nIntegers(N)
    random.shuffle(integers)
    return integers


def nearly_sorted_integers(N):
    integers = nIntegers(N)
    for i in range(0,N):
            if i in [0, N-1]: #jeśli pozycja liczby wynosi 0 lub N-1 to:
                index = random.randint(0, N-1) 
                integers[i], integers[index] = integers[index], integers[i]
            else: #jeśli pozycja liczby jest inna niż 0 lub N-1 to:
                index = random.randint(i-1, i+1) 
                integers[i], integers[index] = integers[index], integers[i]

    return integers


def nearly_sorted_integers_reversed(N):
    integers = nearly_sorted_integers(N)
    print("Nearly sorted integers: ", integers)
    integers.reverse()
    print("Nearly sorted integers reversed: ", integers)
    return integers


def gaussian_floats(N):
    integers = []
    for i in range(N):
        integers.append(random.gauss(0, 1))
    return integers


def repeating_integers(N, k): #N - tyle wygenerujemy liczb, 
    integers = []  #k-spośród tylu liczb będziemy wybierać liczby do naszej listy
    for i in range(N):
        integers.append(random.randint(0, N - k))
    random.shuffle(integers)
    return integers


