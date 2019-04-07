"Laboratorium 5, Beata Kapusta"

# Zadanie 5.1

def czy_parzyste(x, y):
    "Wypisuje liczby od x do y. Określa czy są parzyste czy nie."
    # uzupełnij
    for a in range(x, y+1):
        if(a%2 == 0):
            print(a, "parzysta\n")
        else:
            print(a, "nieparzysta\n")


print("Podaj liczby:\n")
x = int(input())
y = int(input())
czy_parzyste(x,y)

# Zadanie 5.2

def czy_pierwsze(x):
    "Wypisuje liczby od 1 do x. Określa czy są pierwsze czy złożone (z jakich pierwszych się składają)."
    
    # uzupełnij
    numbers = range(1, x+1)
    primes = [y for y in numbers if len([x for x in range(1, y+1) if y%x==0]) == 2]
    for a in numbers:
        if(a == 1 or a==0):
            print(a, "liczba nie jest ani pierwsza ani złożona\n")
        elif(a in primes):
            print(a, "liczba pierwsza\n")
        else:
            dzielniki = [d for d in range(1,a+1) if a%d==0 and d in primes]
            print(a, "liczba złożona:", dzielniki)



print("Podaj liczbę:\n")
x = int(input())
czy_pierwsze(x)
# Zadanie 5.3

def slownie(liczba):
    "Zwraca podaną liczbę słownie"

    #uzupełnij
    j = ['', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
    n = ['', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście']
    d = ['', 'dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt','siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
    s = ['', 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset', 'siedemset', 'osiemset', 'dziewięćset']
    odmiany = [['', '', ''], ['tysiąc', 'tysiące', 'tysięcy'],
        ['milion', 'miliony', 'milionów'],['miliard', 'miliardy', 'miliardów'],
        ['bilion', 'biliony', 'bilionów'], ['biliard', 'biliony', 'biliardów'],
        ['trylion', 'tryliony', 'trylionów'],
        ['tryliard', 'tryliony', 'tryliardów'],
        ['kwadrylion', 'kwadryliony', 'kwadrylionów'],
        ['kwadryliard', 'kwadryliardy', 'kwadryliardów'],
        ['kwintylion', 'kwintyliony', 'kwintylionów'],
        ['kwintyliard', 'kwintyliardy', 'kwintyliardów'],
        ['sekstylion', 'sekstyliony', 'sekstylionów'],
        ['sekstyliard', 'sekstyliardy', 'sekstyliardów'],
        ['septylion', 'septyliony', 'septylionów'],
        ['septyliard', 'septyliardy', 'septyliardów'],
        ['oktylion', 'oktyliony', 'oktylionów'],
        ['oktyliard', 'oktyliardy', 'oktyliardów'],
        ['nonilion', 'noniliony', 'nonilionów'],
        ['noniliard', 'noniliardy', 'noniliardów'],
        ['decylion', 'decyliony', 'decylionów'],
        ['decyliard', 'decyliardy', 'decyliardów']]

    rzad=0
    wynik=[]
    while (liczba != 0):
        setki = (liczba % 1000) // 100
        dziesiatki = (liczba % 100) // 10
        jednosci = (liczba % 10)
        nastki = 0
        if (dziesiatki == 1) & (jednosci > 0):
            nastki = jednosci
            dziesiatki = 0
            jednosci = 0
        if (jednosci == 1) & ((setki + dziesiatki + nastki) == 0):
            forma = 0
        elif (jednosci > 1) & (jednosci < 5):
            forma = 1
        else:
            forma = 2
        if (setki + dziesiatki + nastki + jednosci > 0):
            zbior = [odmiany[rzad][forma],j[jednosci],n[nastki],d[dziesiatki],s[setki]]
            for a in zbior:
                wynik.insert(0, '%s' (a))
        zbior = []
        rzad = rzad + 1
    print(wynik)

print("Podaj liczbę:")
liczba= int(input())
slownie(liczba)
