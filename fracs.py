
import math

def add_frac(frac1, frac2):
    licznik_nieskr = frac1[0]*frac2[1] + frac2[0]*frac1[1]#licznik jeszcze nieskrócony
    mianownik_nieskr = frac1[1]* frac2[1]#mianownik jeszcze nieskrócony
    gcd = math.gcd(licznik_nieskr, mianownik_nieskr)
    licznik = licznik_nieskr/gcd
    mianownik = mianownik_nieskr/gcd
    return [licznik, mianownik]

def sub_frac(frac1, frac2):
    licznik_nieskr = frac1[0]*frac2[1] - frac2[0]*frac1[1]
    mianownik_nieskr = frac1[1]* frac2[1]
    gcd = math.gcd(licznik_nieskr, mianownik_nieskr)
    licznik = licznik_nieskr/gcd
    mianownik = mianownik_nieskr/gcd
    return [licznik, mianownik]


def mul_frac(frac1, frac2):
    licznik_nieskr = frac1[0] * frac2[0]
    mianownik_nieskr = frac1[1] * frac2[1]
    gcd = math.gcd(licznik_nieskr, mianownik_nieskr)
    licznik = licznik_nieskr/gcd
    mianownik = mianownik_nieskr/gcd
    return [licznik, mianownik]


def div_frac(frac1, frac2):
    return mul_frac(frac1, frac2[::-1])


def is_positive(frac):
    if (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0):
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):
    licznik1_nieskr = frac1[0]*frac2[1]
    licznik2_nieskr = frac2[0]*frac1[1]
    #mianownik_nieskr = frac1[1]* frac2[1]
    gcd = math.gcd(licznik1_nieskr, licznik2_nieskr)
    licznik1 = licznik1_nieskr/gcd
    licznik2 = licznik2_nieskr/gcd
    #mianownik = mianownik_nieskr/gcd

    if licznik1 > licznik2:
        return 1
    elif licznik1 < licznik2:
        return -1
    else:
        return 0


def frac2float(frac):
    return frac[0] / frac[1]


