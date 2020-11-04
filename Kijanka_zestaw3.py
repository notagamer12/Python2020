#zad. 3.1 Czy podany kod jest poprawny składniowo w Pythonie?
#Jeśli nie, to dlaczego?
"""
a)
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

Kod jest poprawny, jednak można wprowadzić kilka zmian:
wyglądałoby to tak:
"""

x = 2
y = 3
if x > y:
    result = x
else:
    result = y


"""
b)
for i in "qwerty": if ord(i) < 100: print (i)

Kod nie jest poprawny (nie kompiluje się).
Jak można go poprawić:
"""

for i in "qwerty":
    if ord(i) < 100:
        print (i)
"""



c)
for i in "axby": print (ord(i) if ord(i) < 100 else i)

Kod jest poprawny, jednak można wprowadzić jedną zmianę:
wyglądałoby to tak:
"""

for i in "axby":
    print (ord(i) if ord(i) < 100 else i)
    
"""



#zad. 3.2 Co jest złego w kodzie:
a)

L = [3, 5, 4] ; L = L.sort()
Kod się kompiluje, jednak niczego nie zwraca, ponieważ funkcja L.sort()
sortuje tą samą listę, na której została wywołana. Należałoby wprowadzić zmiany.
Wyglądałoby to tak:
"""

L=[3,5,4]
L.sort()
print(L)
"""
b)
x, y = 1, 2, 3
Kod nie jest poprawny (nie kompiluje się).
Powód błedu:
-przypisanie trzech wartości do dwóch zmiennych. Przy takim przypisywaniu
musi być tyle samo zmiennych, co wartości do nich przypisywanych.

Poprawny byłby na przykład kod:
"""
x,y = 1,2

"""
c)

X = 1, 2, 3 ; X[1] = 4

Kod jest niepoprawny (nie kompiluje się).
Powód błędu:
- dokonano zmiany wartości wewnątrz obiektu niemodyfikowalnego - tuple.
Poprawny byłby kod, w którym tworzymy krotkę od początku, jeśli chcemy zmienić jakąś wartość
"""

X=1, 2, 3
X=X[0], 4, X[2]
"""
d)
X = [1, 2, 3] ; X[3] = 4

Kod jest niepoprawny (nie kompiluje się), ponieważ odwołujemy się do elementu spod indeksu spoza listy.
Listy w pythonie indeksowane są od 0, a ostatni element listy ma indeks n-1, gdzie n to długość listy.
Poprawny kod wyglądałby tak:
"""
X = [1, 2, 3]
X[2] = 4
print(X)

"""
e)
X = "abc" ; X.append("d")

Kod jest niepoprawny ( nie kompiluje się), ponieważ użyto funkcji append na napisie, a funckja append
działa na listach.
Poprawny byłby kod:
"""

X = "abc"
X = X + "d"
print(X)
"""
f)
L = list(map(pow, range(8)))
Kod jest niepoprawny (nie kompiluje się), ponieważ:
-w funkcji pow() nie podano argumentów (a powinny być podane dwa)
-do map() przekazujemy funkcję, która przyjmuje te argumenty, które przekażemy do map() po tej funkcji.
Rozwiązaniem tego problemu byłoby napisanie własnej osobnej funkcji wykonującej podnoszenie do wybranej potęgi (np. do kwadratu) liczb od 0 do 7
i przekazanie tej funkcji do map()
Poprawny byłby na przykład kod:
"""
def secondPower(n):
    return n**2

print(list(map(secondPower, range(8))))

"""
zad. 3.3 Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
"""
for i in range(31):
    if i%3!=0:
        print(i)
"""
zad. 3.4 Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący parę x i trzecią potęgę x.
Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać komunikat o błędzie i kontynuować pracę.
"""

while(True):
    fromstdin=input("Proszę wpisać liczbę rzeczywistą lub stop, by zatrzymać program \n")
    if fromstdin!= "stop":
        try:
            x = int(fromstdin)
        except ValueError:
            print("Podano złą wartość. Proszę wpisać liczbę")
        else:
            print("Podana liczba ", x, " podniesiona do trzeciej potęgi to: ", x ** 3)
    else:
        break

print("zakończono program przez stop")
"""
zad. 3.5 Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
Należy zbudować pełny string, a potem go wypisać.
"""
UNIT_LEN = 10

length = int(input("Podaj długość: \n"))


for i in range(length+1):
    if i == 0:
        finalstr = "|"
    else:
        finalstr += " . . . . |"

finalstr += '\n'

for i in range(length+1):
    if i == 0:
        finalstr+= "0"
    else:
        convertedNumber = str(i)
        space= ''.rjust(UNIT_LEN - len(convertedNumber), ' ')
        finalstr += space+convertedNumber

print(finalstr)
"""
zad. 3.6 Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać.
"""
inputx = int(input("Podaj długość prostokąta: \n"))
inputy = int(input("Podaj szerokość prostokąta: \n"))
result = ""
for i in range ((2*inputy)+1):
    if i%2 == 0:
        for j in range (inputx+1):
            if j == 0:
                result += "+"
            else:
                result += "---+"
    
    else:
        for k in range (inputx+1):
            if k == 0:
                result+= "|"
            else:
                result+= "   |"
    result+="\n"

print(result)
"""
zad. 3.8 Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

a):
"""
L1 = [1, 2, 3, 8, 12, 2, 4]
L2 = [10, 54, 2, 3, 4, 20, 5]

La=[]


for i in L1:
    for j in L2:
        if i == j and (i not in  La):
            La.append(i)


print('Lista bez powtórzeń zawierająca elementy występujące w obu sekwencjach', La)
#b):

L1.extend(L2)
extendedL1Set = set(L1)

print("Lista bez powtórzeń zawierająca elementy z obu sekwencji", extendedL1Set)

"""
zad. 3.9 Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18]
"""
lista = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
suma = []

for i in lista:
    suma.append(sum(i))

print(suma)
"""
zad. 3.10 Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
(podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""


def roman2DecimalBasic(rnumber): #po prostu zamienia symbol rzymski na odpowiadająca mu liczbę arabską w podanym ciągu rzymskich znaków, 
    #ale nie wykonuje żadnych operacji sumy lub różnicy,więc to jeszcze nie jest konwersja liczby rzymskiej na arabską i podanie wyniku
    numbers = []
    for i in rnumber:
        if i == 'M':
            numbers.append(1000)
        elif i == 'D':
            numbers.append(500)
        elif i == 'C':
            numbers.append(100)
        elif i == 'L':
            numbers.append(50)
        elif i == 'X':
            numbers.append(10)
        elif i == 'V':
            numbers.append(5)
        elif i == 'I':
            numbers.append(1)
    return numbers


def roman2int(rnumber): #sumuje liczby rzymskie według zasad i daje wynik
    outcome = 0
    numbers = roman2DecimalBasic(rnumber)

    for ind in range (0, len(numbers)):
        if numbers[ind] == "skip":
            continue #jeśli trafimy na konieczność odejmowania symboli, to nie będziemy dodawać do wyniku następnego symbolu - tego mniejszego (bo to jego odejmowaliśmy od symbolu większego)
        if  numbers[ind] < numbers[ind + 1]:
            outcome += (numbers[ind + 1] - numbers[ind])
            numbers[ind+1] = "skip" #to jest następnik bieżącego symbolu. Odjęliśmy go od bieżącego symbolu, więc oznaczamy go, by w następnej iteracji wiedzieć, że mamy go pominąć
        elif numbers[ind] >= numbers[ind + 1]: 
            outcome +=  numbers[ind]

    return outcome
print("Proszę podać liczbę rzymską do przetłumaczenia na arabską: \n")
roman = input()
print(roman2int(roman))


