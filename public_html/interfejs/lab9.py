# -*- coding: utf-8 -*-

"""
Laboratorium 9, Beata Kapusta
"""

#------------------------------------------------------------------------------

#moduł matematyczny
def dodawanie(liczby):
    """
    zwaraca sume podachych liczb
    """
    suma=0
    for i in liczby:
        suma = suma +i
    return suma

#print(dodawanie(2,3))
print(dodawanie([3,4,5]))

def mnozenie(liczby):
    """
    zwaraca iloraz podachych liczb
    """
    suma=1
    for i in liczby:
        suma = suma*i
    return suma

#print(mnozenie(2,3))
print(mnozenie([3,4,2]))
#print(mnozenie(2, [3,4,5]))

#moduł sortowanie
def po_pierwszym(lista):
    """
    sortuje po pierwszym elemencie
    """
    a = 0
    for i in lista:
        for j in i:
            if type(j) == str:
                a+=1
                break
    if a > 0:
        return print("W twojej liście jest napis, zamień go na liczbę i spróbuj ponownie")
    else:
        return sorted(l, reverse=True)


l = ([5,4], [3,9], [1,2])
print(po_pierwszym(l))
#print(po_pierwszym(l, reverse=True))

def po_drugim(lista):
    """
    sortuje po drugim elemencie
    """
    a = 0
    for i in lista:
        for j in i:
            if type(j) == str:
                a += 1
                break
    if a > 0:
        return print("W twojej liście jest napis, zamień go na liczbę i spróbuj ponownie")
    else:
        return sorted(l, key=lambda t: t[1], reverse=True)


l = ([5,4], [3,9], [1,2])
print(po_drugim(l))
#print(po_drugim(l, reverse=True))


#moduł ???
def parzyste(cyfra):
    """
    Czy liczba jest parzysta
    """
    for i in range(cyfra):
        if i % 2 == 0:
            yield i

c=parzyste(10)
for i in range(1,6):
    print(next(c))

def silnia(cyfra):
    """
    Obliczanie silni
    """
    if cyfra>1:
        return cyfra*silnia(cyfra-1)
    elif cyfra in (0,1):
        return 1

print(silnia(20))
