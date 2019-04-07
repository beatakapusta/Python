"Laboratorium 3, Beata Kapusta"

#------------------------------------------------------------------------------
print('\nZadanie 3.1\n')

a, b, c = 1, -12, 35
# ma działać dla dowolnych a, b, c

# wprowadzanie a, b, c
print('Podaj a:\n')
q = input()
a = int(q)
print('Podaj b:\n')
w = input()
b = int(w)
print('Podaj c:\n')
e = input()
c = int(e)

delta = b ** 2 - 4*a*c           # zastąp zero wzorem na deltę
pierwiastek = delta ** 0.5

# Wypisz równanie


d = 'x^2'
e = 'x'
z = '+'

i = '='
r = 0
print('Równanie:', str(a)+d, z, str(b)+e, z, c, i, r)


# Wypisz rozwiązania
if delta > 0:
    x_1 = (-1*b - pierwiastek) /( 2*a)            # zastąp zero wzorem na rozwiązanie nr 1
    x_2 = (-1*b + pierwiastek) / (2*a)            # zastąp zero wzorem na rozwiązanie nr 2

    print ('Rozwiązania: ', 'x_1 = ', x_1, ', ', 'x_2 = ', x_2)
elif delta == 0:
     x_1 = (-1*b - pierwiastek) /( 2*a)            # zastąp zero wzorem na rozwiązanie nr 1
   
     print('Rozwiązanie: ', 'x_1 = x_2 = ', round(x_1, 2)) 
else:
    print('Rozwiązania: brak')


#------------------------------------------------------------------------------
print('\nZadanie 3.2\n')

n, p = 60, 37
# ma działać dla dowolnych n i p
print('Podaj  2 liczby:')
n = int(input())
p = int(input())
# Wypisz dzielniki n
print('Dzielniki liczby ', n, ': ', [x for x in range(1, n+1) if n % x == 0])

# Wypisz dzielniki p
print('Dzielniki liczby ', p, ': ', [x for x in range(1, p+1) if p % x == 0])

#------------------------------------------------------------------------------
print('\nZadanie 3.3\n')

limit = 100
numbers = range(1, limit+1)

# Zastąp pustą listę wyrażeniem zwracającym liczby pierwsze z zakresu od 1 do 'limit'
primes = [y for y in numbers if len([x for x in range(1, (y//2)+1) if y % x == 0]) == 1]

print('Liczby pierwsze od 1 do %d: %s' % (limit, primes))
