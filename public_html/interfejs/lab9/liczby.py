"""
Laboratoriuum 9, Beata Kapusta
"""



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
                             
