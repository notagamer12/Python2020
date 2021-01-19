import numpy as np
import math
import copy
from numpy import linalg
import sys
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt    

"""
Uwaga - w ponizszych komentarzach uzywam skrotu myslowego
-punkt d, czy tez alfa, okreslam jako minimum kierunkowe funkcji jednej zmiennej.
Chodzi mi o to, ze alfa jest punktem, w ktorym znajdujemy minimum kierunkowe
funkcji jednej zmiennej.
-punkt x okreslam jako kolejne przyblizenie minimum funkcji Rosenborcka.
Chodzi mi o to, ze x jest punktem, w ktorym znajdujemy kolejne przyblizenie
minimum funkcji Rosenbrocka.

"""
def bisection(a,c):                   #funkcja uzywana w metodzie Brenta
    return (a + c)/2.0
  

def parabolic_interpolation(g,a,b,c): #funkcja uzywana w metodzie Brenta.
                                      #Znajduje punkt d, czyli minimum kierunkowe (alfa) funkcji jednej zmiennej (funkcji g)
    numerator= ((g(c)-g(b))*a**2)+((g(a)-g(c))*b**2)+((g(b)-g(a))*c**2)
    denominator= ((g(c)-g(b))*a)+((g(a)-g(c))*b)+((g(b)-g(a))*c)
    try:                              #wylapanie i obsluzenie bledu dzielenia przez 0, jesli taki by nastapil
        d=0.5*(numerator/denominator)
    except Exception as e:
        print(sys.exc_type)
        print(e)
    return d

def new_bracket(g,a,b,c,d): #funkcja uzywana w metodzie Brenta.
                            #Lokalizuje ona wstepny przedzial szukania minimum dla nowo znaleznionego punktu "d"
    gd=g(d)                 #czyli dla nowego minimum funkcji jednej zmiennej (funkcji g) 
    gc=g(c)
    gb=g(b)
    ga=g(a)
    if gd < gb:
        if d<b:
            c=b
            b=d
            gc = gb
            gb = gd
       
        elif d>b:
            a = b
            b = d
            ga = gb
            gb=gd
    elif gd > gb:
        if  d<b:
            a=d 
            ga = gd
        elif d>b:
            c = d
            gc = gd

    return a,b,c
    
#brent to funkcja wykonujaca minimalizacje funcji jednej zmiennej
def brent(g,a,b,c,tol): #za pomocą while(true) i warunku if not + break nasladujemy petle "do while", ktorej nie ma w pythonie
    while True:         #Jest to potrzebne, poniewaz warunek, ktory jest w "if not" wymaga
        d=parabolic_interpolation(g,a,b,c)# wartosci d obliczonej  na zasadach funkcji Brenta
        aOld=a
        cOld=c
        bOld=b
        if a<d<c:
            a,b,c = new_bracket(g,a,b,c,d)
            if ((c-a) >=  (1.0/2.0)*(cOld-aOld)):
                a = aOld
                b = bOld
                c = cOld
                d=bisection(aOld,cOld)
                a,b,c = new_bracket(g,a,b,c,d)
        if not abs((c-a) - (cOld - aOld)) > tol:
            break
    gd = g(d)               
    return d,gd

def bracket(g,a,b,step):#funkcja potrzebna do metody Powella. Lokalizuje ona wstepny przedzial szukania minimum
    for i in range (100): # Szukamy w petli trzech punktow spelniajacych warunek minimum
        if g(a) > g(b):#kierunek spadku
            c = b + step
        else:
            c = b
            b = a
            a = a - step
                    
        ga = g(a)
        gb = g(b)
        gc = g(c)
        if ga>gb and gc>gb:#//Warunek minumum
            break       
        else: 
            step = ((step) * (2.0))

    return a,b,c
    
"""
opis do funkcji powell - glownej funkcji programu:
Ta funkcja wylicza globalne minimum funckji Rosenbrocka
startujac z punktu [-3, 4]. Szukanie tego minimum odbywa sie w taki sposob, ze
wykonujemy  "j" cykli poszukiwania minimum funkcji rosenbrocka. W każdym cyklu zachodzi obliczenie
w petli for n nowych przyblizen minimum fcji Rosenbrocka (wzdluz kolejnych niesprzezonych kierunkow pi),
a nastepnie obliczenie za pomoca ostatnio wyliczonego przyblizenia minimum, czyli x(n)
nowego, SPRZEZONEGO kierunku poszukiwan, czyli p(n). Idac w tym sprzezonym kieruku p(n) otrzymujemy x(n+1)
W nowym cyklu naszym x0, od ktorego starutjemy petle for, jest x(n+1) wyliczone w poprzednim cyklu.
Celem nowego cyklu (tak samo jak poprzednoego) jest obliczenie nowego sprzezonego kierunku
poszukiwan (p(n)) i obliczenie nowego przyblizenia minimum funckji Rosenbrocka (x(n+1)).
Dlaczego w kazdym cyklu poszukujemy sprzezonego kierunku? Poniewaz idac po kierunkach sprzezonych
mozemy najszybciej osiagnac minimum funckji Rosenbrocka.
Nowo znaleziony sprzezony kierunek p(n)-(conjugate direction)
zapisujemy w macierzy "u" przechowujacej kierunki, a kierunek, ktory dal nam najwiekszy spadek przy minimalizacji
jednowymiarowej wyrzucamy z tej macierzy "u". Ten zabieg sprawi, ze kolejne kierunki
nie beda od siebie liniowo zalezne (rownolegle). Liniowo zalezne kierunki sprawily by,
ze wolniej bedziemy sie zblizac do prawdziwego minimum funkcji Rosenbrocka.

Wazne jest to, wykonujac minimalizacje w kolejnych kierunkach
robimy minimalizacje jednowymiarowej, pomocniczej funkcji g,
wyrazonej wzorem: g(alfa) = f(x + alfa*p)
Te jednowymiarowe minimalizacje za kazdym razem sa przeprowadzone za
pomoca metody Brenta (tej metodzie podajemy przedzial wstepnej lokalizacji minimum.
Ten przedzial obliczony jest za pomoca funkcji :bracket"). 
================================================================================
-f to funkcja Rosenbrocka a g to fcja jednej zmiennej
-n to ilosc zmiennych funkcji f. Tutaj n to 2, bo funkcja
Rosenbrocka ma dwie zmienne: x i y
-macierz A przechowuje wartosci funkcji Rosenbrocka w kolejnych punktach
bedacych przyblizeniami minimum (obliczanymi w kolejnych iteracjach zliczanych przez "j")
-u to macierz jednostkowa (tzn. jest wypelniona zerami i ma jedynki na przekatnej) o wymiarach n x n
Ta macierz zbudowana jest z kolejnych wersorow (poczatkowe kierunki poszukiwan wzdluz wspolrzednych),
ale w miare dzialania funkcji macierz ta wypelnia sie kolejnymi znalezionymi kierunkami
poszukiwan minimum (wektory p)
-xOld  = [0,0 ] jest to wartosc poczatkowa potrzebna jedynie do wystartowania petli while
-xOld w petli while to wartosc przyblizenia minimum funkcji Rosenbrocka
z poprzedniej iteracji
-j= liczy, ile cykli zajelo szukanie minimum funkcji Rosenbrocka
"""

def powell(f,x,step,tol): 
    def g(alfa): return f(x + alfa*p) 
    n = len(x)
    A = np.empty([0, n])
    u = np. identity(n)
    df = np.zeros(n)
    xOld = [0, 0] 
    j = 0
    while linalg.norm(xOld-x)>tol: 
        xOld = x.copy() #punkt xOld to x(n+1) znaleziony w poprzednim cyklu, ktory teraz staje sie x0, bo od niego zaczynamy nowy cykl
        gOld = f(xOld)#na poczatku nie ma ani alfa ani nie ruszylismy w zadnym kierunku p
        for i in range(n):#minimalizacja wzdluz kolejnych kierunkow pi osiagajac kolejno punkty xi - kolejne przyblizenia minimum funkcji f
            p = u[i] #pierwszy kierunek poszukiwan to wersor [1,0]. 
            q = x[0]
            w = q+step
            a,b,c = bracket(g,q,w,step)#przedzial, w ktorym szukamy minimum funkcji g to (x[0], x[0]+step)		
            alfa,gMin = brent(g,a,b,c,tol)
            df[i] = gOld - gMin #obliczanie spadku kolejnego przyblizenia minimum
            gOld = gMin
            x = x + alfa*p 
        #obliczenie nowego kierunku p(n+1) za pomoca znalezionego w petli for punktu x(n)   
        p = x - xOld #nowo znaleziony kierunek poszukiwania minimum - p(n+1)
        q = x[0]#nowo znalezione przybliżenie minimum funkcj g
        w = q+step
        a,b,c = bracket(g,q,w,step)#minimalizacja wzdluz nowo znalezionego kierunku p(n+1), osiagajac nowy punkt x(n+1)
        alfa,gLast = brent(g,a,b,c,tol)
        x = x + alfa*p #nowo znaleziony punkt x(n+1) - wpisujemy go do macierzy A jako kolejne przyblizenie minimum
        A = np.append(A, np.array([x]), axis=0) #wiersz j-ty macierzy A.
        iMax = np.argmax(df)
        for i in range(iMax,n-1):
            u[i] = u[i+1]#pozbywamy się kierunku dla ktorego osiagniety byl najwiekszy spadek, by uniknac zaleznosci liniowej kierunkow 
        u[n-1] = p#nowo wyliczony kierunek p(n) wpisujemy do macierzy przechowujacej kolejne kierunki sprzezone
        print("new conjugate direction: ", u[n-1])
        j+=1
    return x,j,A
	

def f(x): return 100.0*(x[1] - x[0]**2)**2 + (1 - x[0])**2
xStart = np.array([-3.0, -4.0]) #startujemy z punktu (-3,-4)
xMin,nIter,A = powell(f,xStart,0.1,1.0e-9)
print("\n")
print("Minimum of Rosenbrock function =",f(xMin))
print("Point, in which minimum of Rosenbrock function was found =",xMin)
print("How many cycles did it take: ",nIter)
print("\n")
print("Points in which were finding next approximations of global minimum: ")
print(A)
print("\n")

#################################### RYSOWANIE WYKRESU FUNKCJI ROSENBROCKA ORAZ KOLEJNYCH PRZYBLIZEN MINIMUM GLOBALNEGO TEJ FUNKCJI ############################
    
fig = plt.figure()
ax = plt.axes(projection="3d")

def z_function(x, y):
    return 100.0*(y - x**2)**2 + (1 - x)**2

y = np.linspace(0, 3, 300)
x = np.linspace(-2, 2, 300)
X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='green',alpha=0.4)

fx = []# fx to tablica przechowujaca wartosci funkcji rosenbrocka w kolejnych punktach bedacych przyblizeniami minimum

for j in range (nIter):
    fx.append(z_function(A[j][0], A[j][1])) #kolumna 0 to wartosci z ox, kolumna 1 to wartosci z oy

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#kolumna 0 macierzy A to wartosci z ox, kolumna 1 z macierzy A to wartosci z oy, fx to wartosci z oz
ax.scatter(A[:,0],A[:,1],fx,s=10,c='r',marker='o')
plt.show()


#################################### TEST OBLICZENIA MINIMUM GLOBALNEGO FUNKCJI ROSENBROCKA #######################################3 
if abs(f(xMin) - 0) >= 0.000001 and linalg.norm(xMin -[1, 1])>= 0.000001 : 
    print("Program failed to calculate the true minimum of Rosenbrock function") 
else: 
    print(f(xMin),"is close enough  to the true minimum of Rosenbrock function, which is 0, and program calculated correctly, that the minimum is in point ", xMin)




