"""
Laboratorium 9, Beata Kapusta
"""


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



