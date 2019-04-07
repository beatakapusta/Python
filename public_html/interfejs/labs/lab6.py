# -*- coding: utf-8 -*-

"""
Laboratorium 6, Beata Kapusta
"""

#------------------------------------------------------------------------------
a = 10 # definicja zmiennej globalnej a.

def print_global():
    """
    funkcja print_global(), która wypisuje zmienną globalną a.
    """
    print(a)

def shadow_a():
    """
    przypisauje wartość 20 do zmiennej lokalnej a.
    """
    a = 20
    def inner():
        """
        wypisuje wcześniej utworzoną zmienną globalną a
        """
        print_global()
    inner()

def complicated():
    """
    wywołuje wewnętrzną funkcję f1(), która definuje zmienną lokalną x na 7 a na sam koniec na 8
    i wywołuje wewnętrzną funkcję f2() wypisującą zmienną x (równą 8)
     i wywołującą wewnętrzną funkcję funkcji complicated - funkcję f0(), która ustwia zmienną lokalną x na 6 i ją wypisuje
    potem funkcja f2() wypisuje zmienną lokalną x-1 (8-1=7)
    """

    x = 5
    def f0():
        x = 6
        print(x)
    def f1():
        x = 7
        def f2():
            print(x)
            f0()
            print(x-1)
        x = 8
        f2()
    f1()

counter = 1
def increase_counter(n):
    """
    Funkcja increase_counter(n) zwiększa wartość zmiennej counter o n.
    """
    global counter
    counter = counter + n
    print(counter)

def make_dict_adder():
    """
    tworzy i zwraca funkcję add(key, value),
    dodającą do słownika nową parę klucz-wartość i zwracającą słownik po modyfikacji
    """
    
    def add(key,value):
        """
        dodaje do słownika nową parę klucz-wartość i zwracaja słownik po modyfikacji
        """
        add.slownik[key]=value
    
    add.slownik = {}

    return add


