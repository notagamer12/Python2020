import random
import math
#zad. 8.1
def solve1(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Równanie tożsamościowe")
            elif c != 0:
                print("Równanie sprzeczne. Brak rozwiązań")
        elif b != 0:
            if c == 0:
                print("Rozwiązanie: y = 0")
            elif c != 0:
                print("Rozwiązanie: y = ", -c/b)
    elif a != 0:
        if b == 0:
            if c == 0:
                print("Rozwiązanie: x = 0")
            elif c !=0: 
                print("Rozwiązanie: x = ", -c/a)
        elif b != 0:
            if c == 0:
                print("Rozwiązanie: y = ", -a/b, "* x")
            elif c != 0:
                print("Rozwiązanie: y = ", -a/b, "* x + (", -c/b, ")")


#zad. 8.3
#ilosc trafień w koło oznaczylam przez Nt,
#a przez N oznaczylam ilosc wszystkich strzalow
#n to liczba losowanych punktów
def calc_pi(n=100):
    N=0
    Nt=0
    PI=0

    for i in range (n):
        x = random.random()
        y = random.random()
        odleglosc = x * x + y * y 
        if (odleglosc <= 1): # bo 1 to (promień koła)^2
            Nt+=1
        N = N + 1
        PI = 4*(Nt/N) #PI=PoleCwiartkiOkregu*4
        print("przyblizenie liczby PI dla N= ", N, " wynosi: ", PI)
    return PI

#zad. 8.4
def triangleCondition(a, b, c):   
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True


def heron(a, b, c):
    if not triangleCondition(a, b, c):
        raise ValueError("Z podanych boków nie da się zbudować trójkąta")
    else: 
        p = (a + b + c) / 2
        triangle_area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return triangle_area


#zad. 8.6
def dynamic_Pij(i, j): #dynamicznie
    
    function_args_and_values = {(0, 0): 0.5, (1, 0): 0, (0, 1): 1, (1, 1): 0.5 }
    # początkowe wartości i oraz j to 1, gdy i oraz j mają być >0
   
    if (i, j) in function_args_and_values.keys():
        return function_args_and_values.get((i, j))
    elif j == 0:
        return function_args_and_values.get((1, 0))
    elif i == 0:
        return function_args_and_values.get((0, 1))
    elif i > 0 and j > 0:
        function_args_and_values[(i, j)] = 0.5 * (dynamic_Pij(i - 1, j) + dynamic_Pij(i, j - 1))
        return function_args_and_values.get((i, j))


def recurrent_Pij(i, j): #rekurencyjnie
    if i == 0 and j == 0:
        return 0.5
    elif i > 0 and j == 0:
        return 0.0
    elif i == 0 and j > 0:
        return 1.0
    elif i > 0 and j > 0:
        return 0.5 * (recurrent_Pij(i - 1, j) + recurrent_Pij(i, j - 1))

#porównanie wersji dynamicznej i rekurencyjnej
print(dynamic_Pij(2, 1))
print(recurrent_Pij(2, 1))
