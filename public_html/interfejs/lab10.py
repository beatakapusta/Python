# -*- coding: utf-8 -*-

"""
Laboratorium 10, Beata Kapusta
"""

#------------------------------------------------------------------------------

"""
Klasa Osoba.
"""
class Osoba():
    def __init__(self, imie, nazwisko, wiek, plec):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.plec = plec

    def __repr__(self):
        return 'Dane studenta: %s %s, lat %r' % (self.imie, self.nazwisko, self.wiek)

"""
Klasa Student.
"""
class Student(Osoba):
    def __init__(self, imie, nazwisko, wiek, plec, kierunek):
        Osoba.__init__(self, imie, nazwisko, wiek, plec)
        self.oceny = []
        self.stypendium = False
        self.kierunek = kierunek

    def __repr__(self):
        return 'Otrzymuje stypendium: %r' % (self.stypendium)

    """
    Funkcja dodaj_ocene umożliwia dodanie oceny studenta.
    """
    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    """
    Funkcja nadaj_stypendium nadaje stypendium studentowi.
    """
    def nadaj_stypendium(self):
        l = len(self.oceny)
        o = 0
        if l > 0:
            for i in self.oceny:
                o = o + i
            s = o/l
            if s > 4.5:
                self.stypendium = True
        else:
            print('Brak ocen w systemie.')

"""
Klasa Wykładowca.
"""
class Wykladowca(Osoba):
    def __init__(self, imie, nazwisko, wiek, plec,stanowisko, pensja, urlop, nrpokoju):
        Osoba.__init__(self, imie, nazwisko, wiek, plec)
        self.stanowisko = stanowisko
        self.pensja = pensja
        self.urlop = urlop
        self.nrpokoju = nrpokoju

    def __repr__(self):
        return '%s %s pracuje na stanowisku %s.' % (self.imie, self.nazwisko, self.stanowisko)

    """
    Funkcja zmienstan zmienia stanowisko pracownika.
    """
    def zmienstan(self, stan):
        self.stanowisko = stan


s = Student('Jan', 'Kowalski', '22', 'M', 'informatyka')
w = Wykladowca('Aleksandra', 'Nowak', '40', 'K', 'adiunkt', '4000', 'N', '203')
