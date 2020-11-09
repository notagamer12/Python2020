#zad 4.2
#Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji,
#które zwracają pełny string przez return.
#Ad. 3.5)
UNIT_LEN = 10

def miarka(length):
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
    return finalstr

print("Funkcja rysująca miarkę")
length = int(input("Podaj długość: "))
print(miarka(length))

#ad. 3.6)

def kratki(inputx, inputy):
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
    return result
inputx = int(input("Podaj długość prostokąta: \n"))
inputy = int(input("Podaj szerokość prostokąta: \n"))
print(kratki(inputx, inputy))

#zad. 4.3 Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result* i
    return result
n=int(input("Podaj liczbę, której silnię chcesz obliczyć: \n"))
print(factorial(n))

#zad. 4.4 Napisać iteracyjną wersję funkcji fibonacci(n)
#obliczającej n-ty wyraz ciągu Fibonacciego.
def Fibonacci(n):
    #ciagFib = [(0)[1,1,2,3,5,8,13...]
    ciagFib=[]
    a0=0
    a1=1
    ciagFib.extend([a0,a1])
    for i in range (2, n+1):
        an = ciagFib[i-2]+ciagFib[i-1]
        ciagFib.append(an)
    result=ciagFib[n]
    return result
    
n=int(input("Podaj numer wyrazu z ciągu Fibonacciego, który chcesz obliczyć: \n"))
print(Fibonacci(n))

#zad 4.5 Napisać funkcję odwracanie(L, left, right)
#odwracającą kolejność elementów na liście od numeru left do right włącznie.
#Lista jest modyfikowana w miejscu (in place).
#Rozważyć wersję iteracyjną i rekurencyjną.

def odwrRekur(L, left, right):
    L[left], L[right] = L[right], L[left]
    if (left == right) or (right-left==1):
        print(L)
    else:
        left = left+1
        right = right -1
        odwrRekur(L,left,right)
        
def odwrIter(L, left, right):
    odwrLen = (right-left)+1
    Lc = L.copy()
    for i in range(odwrLen):
        L[left+i]=Lc[right-i]
    print(L)
    
        
    
    

L=[1,2,3,4,5,6,7]
#gdy odwrócę wybraną część listy L przez funkcję rekurencyjną...
odwrRekur(L, 2,5)
#to gdy do tej samej listy zastosuję drugą funkcję odwracającą...
odwrIter(L,2,5)
#to dostanę wyjściową listę L


#zad. 4.6 Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych
#w sekwencji, która może zawierać zagnieżdżone podsekwencje. Wskazówka: rozważyć
#wersję rekurencyjną, a sprawdzanie czy element jest sekwencją,
#wykonać przez isinstance(item, (list, tuple)).

def sumSeq(sequence):
    itemsSum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            itemsSum = itemsSum + sumSeq(item)
        else:
            itemsSum += item
    return itemsSum

sequence = [1, [2, 3], 4, (5, 6), [(7,8), [9]], []]
print("Suma elementów sekwencji: ", sumSeq(sequence))

#zad. 4.7 Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami,
#a takie zagnieżdżenia mogą się nakładać do nieograniczonej głębokości.
#Napisać funkcję flatten(sequence),która zwróci spłaszczoną listę wszystkich elementów sekwencji.
#Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją,
#wykonać przez isinstance(item, (list, tuple)).
def flatten(result, seq):
    for item in seq:
        if isinstance(item, (list, tuple)):
            flatten(result, item)
        else:
            result.append(item)
    return result

result=[]
seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print("Spłaszczona lista: ", flatten(result, seq))

        
        
