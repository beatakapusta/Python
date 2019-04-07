"""
Laboratorium 7, Beata Kapusta
"""

#------------------------------------------------------------------------------
import lab6

def call(funkcja, *args, **kw_args):
     '''
     funkcja, która potrafi wywołać dowolną funkcję z dowolnymi argumentami
     '''
     return funkcja(*args, **kw_args)

print(call(sorted, [1, 3, 2], reverse=True))
print(call(max, 4, -5, 3))
print(call(max, 4, -5, 3, key=lambda x: abs(x)))
print(call(sorted, [1, 3, 2], reverse=True))

def add_to_dict(key, value, slownik=None):
     '''
     funkcja add_to_dict dodającą parę klucz-wartość do słownika
     '''
     if slownik is None:
        slownik = {}
     slownik[key] = value
     return slownik

print(add_to_dict(1, 2))
print(add_to_dict('a', 'b'))
print(add_to_dict('c', 'd', {5: 6}))
d = {'x': 'y'}
print(add_to_dict(10, 20, d))
print(d)



slowa = lambda zdanie: zdanie.split()
zdanie= "To jest zdanie"
print(slowa(zdanie))

def czy_parzyste(a,b):
    for x in range(a, b+1):
        werdykt = lambda x: "parzysta\n" if x%2 == 0 else "nieparzysta\n"
        print(x,werdykt(x))

print("Podaj liczbę początkową i końcową zakresu:")
a = int(input())
b = int(input())
czy_parzyste(a,b)




