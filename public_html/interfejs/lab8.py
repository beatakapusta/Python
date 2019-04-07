"""
Laboratorium 8, Beata Kapusta
"""

#------------------------------------------------------------------------------
def fib_gen():
    """
    Zwracaja kolejne wartości ciągu Fibonacciego przy pomocy wyrażenia yield.
    """
    a = 0
    b = 1
    yield a
    yield b

    while True:
        yield (a+b)
        a,b = b, (a + b)

f = fib_gen()
for i in range(1,10):
    print(next(f))

def get_values(iterator, n):
    """
    Zwraca listę n kolejnych wartości pobranych z iteratora.
    """
    licznik = 0
    lista = []
    try:
        while(licznik<n):
            lista.append(next(iterator))
            licznik +=1
    except StopIteration:
        pass
    return lista

i = iter(range(10))
print(get_values(i,3))
print(get_values(i,5))
print(get_values(i,4))
print(get_values(i,4))

#przykład użycia: ciąg Fibonacciego
def next_fibonacci(a, b):
    return a + b

# przykład użycia: ciąg liczb parzystych
def next_even(a):
    return a + 2

def sequence_gen(funkcja, *n):
    """
    generuje kolejne wyrazy dowolnego ciągu danego przy pomocy definicji rekurencyjnej.
    """
    
    kolejny_wyraz = funkcja(*n)
    white(True):
        yield kolejny_wyraz
        kolejny_wyraz = funkcja(*n)
        
g = sequence_gen(next_fibonacci, 0, 1)
for i in range(1,6):
    print(next(g))

h = sequence_gen(next_even, 0)
for i in range(1,5):
    print(next(h))

j = sequence_gen(lambda a,b,c: a+b+c, 0, 0, 1)
for i in range(1,9):
    print(next(j))

f = sequence_gen(lambda a,b: a+b, 'a', 'b')
for i in range(1,10):
    print(next(f))

#dodatkowe
def  next_look_and_say(n):
    """
    zwraca dla danej liczby będącej wyrazem ciągu look-and-say kolejny jego wyraz
    """
    n = str(n)
    l = 1 #licznik
    pierwszy = n[0] #pierwszy znak w n
    result = ''
    for i in range(1,len(n)): #for przez cały napis n
        if pierwszy==n[i]:
            l+=1 # jeśli n[i] jest końcem
        else:
            result = result+str(l)+pierwszy
            l=1
        pierwszy= n[i] #nowy pierwszy znak
    result = result+str(l)+pierwszy
    return result

k = sequence_gen(next_look_and_say, 1)
for i in range(1,9):
    print(next(k))
