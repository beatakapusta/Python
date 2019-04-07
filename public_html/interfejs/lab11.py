# -*- coding: utf-8 -*-

"""
Laboratorium 11, Beata Kapusta
"""

#------------------------------------------------------------------------------

import math

class SquaresGen:
    """Generator kwadratĂłw kolejnych liczb naturalnych.
       MaksymalnÄ liczbÄ wyrazĂłw okreĹla 'limit'.
    """
    def __init__(self, limit):
        self.count = 0
        self.limit = limit

    def __iter__(self):
        "Pobiera iterator, ktĂłrym jest ten sam obiekt"
        element = NextSquaresGen(self.limit)
        return element

    def __next__(self):
        "Zwraca kolejny element ciÄgu"
        self.count += 1
        if self.count > self.limit:
            raise StopIteration
        return self.count ** 2

class NextSquaresGen:
    """
    zwraca nową iteracje
    """

    def __init__(self, limit):
        self.count = 0
        self.limit = limit

    def __next__(self):
        """kolejne elementy"""
        self.count += 1
        if self.count > self.limit:
            raise StopIteration
        return self.count ** 2

class Vector:
    "Wektor w trĂłjwymiarowej przestrzeni euklidesowej."
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return '[%.2f, %.2f, %.2f]' % (self.x, self.y, self.z)

    def __add__(self, vec): #Addition
        "suma: self + vec"
        return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __mul__(self, vec):  #Multiplication
        """
        iloczyn skalarny - vektor a *  wektor b =  (a.x * b.x ) + (a.y* b.y) + (a.z* b.z) = c
        """
        c = (self.x * vec.x) + (self.y * vec.y) + (self.z * vec.z)
        return c

    def norm(self):
        """norma zerowa - długość wektora = pierwiastek z wektor.x^2 + wektor.y^2+ wektor.z^2"""
        norma = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        return norma

    def __bool__(self, x):
        "sprawdzenie czy dł wektora jest niezerowa"
        if x == 0:
            return False
        else:
            return True


    ## def __iadd__(self, vec):
    ##     "suma: self += vec"
    ##     self.x += vec.x
    ##     self.y += vec.y
    ##     self.z += vec.z
    ##     return self

    def __eq__(self, vec):
        return self.x == vec.x and self.y == vec.y and self.z == vec.z

    def __ne__(self, vec):
        return not self == vec

class Point:
    "Punkt w trójwymiarowej przestrzeni euklidesowej."

    def __init__(self, x, y, z): #inincjacja
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return '(%.2f, %.2f, %.2f)' % (self.x, self.y, self.z)

    def __sub__(self, poi): #Subtraction a-b
        vector = Vector(self.x - poi.x, self.y - poi.y, self.z - poi.z)
        return vector

    def __add__(self, vec): #Addition a+b
        return Point(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __iadd__(self, vec): #
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z
        return self

    def __eq__(self, vec): #Equality	 a==b
        return self.x == vec.x and self.y == vec.y and self.z == vec.z

    def __ne__(self, vec): #Difference	a !=B
        return not self == vec

class Triangle:
    "Trójkąt w trójwymiarowej przestrzeni euklidesowej."

    def __init__(self, a, b, c):
        if (a != b) and (a != c) and (b != c):
            self.a = a
            self.b = b
            self.c = c
        else:
            print('Punkty nie mogą sie pokrywać!')

    def __repr__(self):
        return 'triangle: %s, %s, %s' % (self.a, self.b, self.c)

    def perimeter(self):
        #liczę vektory, z których zbutowany jest trójkąt
        vecA = self.b - self.a
        vecB = self.c - self.b
        vecC = self.c - self.a
        suma = vecA.norm() + vecB.norm() + vecC.norm() #liczę długość odc.
        return suma

    def area(self): #1/2 * dł wektora AB * AC
        vecAB = (self.b - self.a).norm() #liczę wektory
        vecAC = (self.a - self.c).norm()
        vecCB = (self.c - self.b).norm()
        p = self.perimeter() / 2
        return (p * (p - vecAB) * (p - vecAC) * (p - vecCB)) ** 0.5


    def __eq__(self, trojkat): #Equality	 a==b
        if type(trojkat) is not Triangle:
            return False
        return self.a == trojkat.a and self.b == trojkat.b and self.c == trojkat.c

    def __ne__(self, trojkat): #Difference	a !=B
        return not self == trojkat

g = SquaresGen(20)
print(list(g))
print(list(g))
v1 = Vector(0, 1, 0)
v2 = Vector(3, 5, 3)
print(v1 * v2)
v1.norm()
v2.norm()
A = Point(0, 1, 0)
print(A)
A = Point(2, 1, 0)
B = Point(0, 1, 1)
print(A - B)
A = Point(0, 1, 0)
v = Vector(3, 4, 5)
print(A + v)
print(id(A))
A += v
print(A)
A += v
print(id(A))
A = Point(0, 0, 0)
B = Point(1, 0, 0)
C = Point(0, 1, 0)
t = Triangle(A, B, C)
print(t)
print(t.perimeter())
print(t.area())

