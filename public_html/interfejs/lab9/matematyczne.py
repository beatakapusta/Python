"""
Laboratorium9, Beata Kapusta
"""


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

