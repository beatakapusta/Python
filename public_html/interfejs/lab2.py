"Laboratorium 2, Beata Kapusta"

#------------------------------------------------------------------------------
print('\nZadanie 2.1\n')

a, b, c = 1, -12, 35
# ma działać dla dowolnych a, b, c, dla których istnieją rozwiązania

delta = b ** 2 - 4*a*c          # zastąp zero wzorem na deltę
pierwiastek = delta ** 0.5
x_1 = (-1*b - pierwiastek) /( 2*a) # zastąp zero wzorem na rozwiązanie nr 1
x_2 = (-1*b + pierwiastek) / (2*a) # zastąp zero wzorem na rozwiązanie nr 2

# Wypisz równanie

d = 'x^2'
e = 'x'
z = '+'

i = '='
r = 0
print( str(a)+d, z, str(b)+e, z, c, i, r)


# Wypisz rozwiązania

print('x_1 =',  x_1, 'x_2 =', x_2)

#------------------------------------------------------------------------------
print('\nZadanie 2.2\n')

print('\nPodaj liczbę\n')
l = input()			# zastąp odpowiednią funkcją
i = int(l)
# Wypisz wprowadzoną liczbę

print(i)

# Wypisz podwojoną

p = 2 * i

print('\nTwoja liczba po podwojeniu to', p)


# Wypisz wiele razy

r = 5 * l
print('\nPowtarzając Twoją liczbę 5 razy otrzymamy:', r)

# Wypisz podzieloną przez 3

d = i / 3

print('\nPodzielona przez 3:', d)

# Wypisz resztę z dzielenia

z = i % 7

print('\nReszta z dzielenia przez 7 to:', z)
#------------------------------------------------------------------------------
