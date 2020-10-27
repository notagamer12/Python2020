#-*-coding: utf-8-*-


#zadanie 2.10
line = """Nie widziałam cię już od miesiąca. 
    I nic. Jestem może bledsza,
trochę śpiąca, trochę bardziej milcząca,
lecz widać można żyć bez powietrza!."""
# w potrójnych cudzysłowach zapisujemy wielowierszowy napis

def licz_slowa(string):
    x= string.strip().replace(",", "").replace(".", "").replace("!", "").split()#usuwamy białe znaki z początku i końca napisu,usuwamy znaki przestankowe,
                                                                                #a następnie wyrazy oddzielone białymi znakami (spacje, tab, \n) zapisujemy kolejno do zmiennej x.
    return(len(x))              #te wyrazy przechowujemy w zmiennej x jako kolejne elementy tej listy



print("Napis zawiera ", licz_slowa(line), " słów")





#################################################################################################################################################
#zadanie 2.11
word="rozdzielanie"
print("Słowo z literami rozdzielonymi znakiem _ wygląda tak: ")
print("_".join(word))





#################################################################################################################################################
#zadanie 2.12 Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich znaków wyrazów z wiersza line.


def napis_z_pierwszych(string):
    first =string.partition('\n')[0] # w first przechowywyany bedzie pierwszy wiersz napisu string
    newStringFirst="" #w newStringFirst przechowywany będzie napis utworzony z ostatnich liter słów z wiersza napisu string

    y= first.replace(",", "").replace(".", "").replace("!", "").split() #rozdzielamy napis f na poszczególne wyrazy. Wyrazy zapisujemy w liście y jako kolejne elementy tej listy

    for words in y: #iterujemy po wszystkich słowach z listy y i do nowego, powstającego napisu dołączamy pierwsze znaki tych słów
        newStringFirst = newStringFirst+words[0]
        
    return newStringFirst

print("Napis utworzony z pierwszych liter słów z wiersza napisu line wyglada tak: ", napis_z_pierwszych(line))




def napis_z_ostatnich(string):
    first=string.partition('\n')[0]
    newStringLast=""
    
    y= first.replace(",", "").replace(".", "").replace("!", "").split()
    
    for words in y: 
        newStringLast = newStringLast+words[len(words)-1]
    
        
    return newStringLast

print("Napis utworzony z ostatnich liter słów z wiersza napisu line wyglada tak: ", napis_z_ostatnich(line))



#################################################################################################################################################
#zadanie 2.13 Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().

def suma(string):
    sumaDlugosciWyrazow = 0
    
    z=string.replace(",", "").replace(".", "").replace("!", "").split() #usuwanie z napisu line wszystkich znaków przestankowych i podzielenie napisu na wyrazy. Zapisanie tych wyrazów w zmiennej z
    
    for words2 in z:
        sumaDlugosciWyrazow = sumaDlugosciWyrazow+len(words2)
        print("Suma to: ", sumaDlugosciWyrazow)
    
        
    return sumaDlugosciWyrazow
print("Suma długości wszystkich wyrazów z napisu line to: ", suma(line))




#################################################################################################################################################
#zadanie 2.14
#Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
def najdluzszy(string):
    
    z=string.replace(",", "").replace(".", "").replace("!", "").split() #usuwanie z napisu line wszystkich znaków przestankowych i podzielenie napisu na wyrazy. Zapisanie tych wyrazów w zmiennej z
    max_dlugosc = 0
    for words2 in z:
        if len(words2) > max_dlugosc: 
            max_dlugosc = len(words2)
            najdluzszywyr = words2
        
    print("najdluzszy wyraz z tekstu line to :", najdluzszywyr, " o dlugosci: ", max_dlugosc)    

najdluzszy(line)




#################################################################################################################################################    
#2.15 Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
L=[211, 30, 45, 8, 1, 99, 100]
def napis_z_liczb(lista):
    napis=""

    for i in lista:
        napis = napis+ str(i)

    return(napis)

print("napis utworzony z liczb z listy L: ",napis_z_liczb(L))


#################################################################################################################################################

#zadanie 2.16 W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum"
lineGvR = """Nie widziałam cię już od miesiąca. 
    I nic. Jestem może bledsza,
trochę śpiąca, trochę bardziej milcząca,
lecz widać można żyć bez powietrza GvR!"""


replaced = lineGvR.replace("GvR", "Guido van Rossum")

print(replaced)




#################################################################################################################################################
#zadanie 2.17 Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().
def sortowanie(string):
    
    z=string.replace(",", "").replace(".", "").replace("!", "").lower().split() #usuwanie z napisu line wszystkich znaków przestankowych, zamiana wielkich liter na małe 
    alfabetycznie = sorted(z)                                                      #i podzielenie napisu na wyrazy. Zapisanie tych wyrazów w zmiennej z
    dlugosciowo = sorted(z, key=len)
    print("Napis posortowany alfabetycznie wyglada tak :", alfabetycznie, " a posortowany pod względem długości wyrazów: ", dlugosciowo)    
#konieczna była zamiana wielkich liter na małe w naszym napisie po to, by móc poprawnie posortować wyrazy alfabetycznie


sortowanie(line)

#################################################################################################################################################
#2.18 Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.
duzaLiczba = 189000020001
duzaLiczbaString = str(duzaLiczba)
print("W naszej liczbie całkowitej znajduje się ", duzaLiczbaString.count('0'), " zer")

#################################################################################################################################################
# 2.19 Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe
#będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().

def wypelnianieZerami():
    listaLiczb = [1, 2, 3, 987, 780, 22, 33, 45, 567]
    listaLiczbString=[]
    for i in listaLiczb: #przerabianie elementow listy z int na string, bo funkcja zfill() działa tylko na napisy
        listaLiczbString.append(str(i))
    
    napisZzerami=""
    for liczby in listaLiczbString:
        napisZzerami= napisZzerami+ liczby.zfill(3)
    
    return napisZzerami

print("Napis złożony z trzycyfrowych bloków wygląda tak: ", wypelnianieZerami())





























