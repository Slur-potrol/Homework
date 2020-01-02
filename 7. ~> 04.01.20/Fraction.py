#!python3
#-*-encoding:utf-8-*-


import math

class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def __repr__(self):
        multiple = self.get_greatest(self.num, self.den)
        if self.num < 1:
            self.num = - self.num
            self.den = - self.den
        if multiple == 0:
            return '{}'.format(0)
        elif multiple / self.num == 1:
            return '{}'.format(int(multiple / self.den))
        else:
            return '{}/{}'.format(
                int(multiple / self.den), int(multiple / self.num)
            )

    def __str__(self):
        multiple = self.get_greatest(self.num, self.den)
        if self.num < 1:
            self.num = - self.num
            self.den = - self.den
        if multiple == 0:
            return 'Fraction({}, {})'.format(0, 0)
        else:
            return 'Fraction({}, {})'.format(
                int(multiple / self.den), int(multiple / self.num)
            )

    def __add__(self, other):
        try:
            return Fraction(
                (self.num * other.den + self.den * other.num), (self.den * other.den)
            )
        except AttributeError:
            return Fraction((self.num + self.den * other), (self.den))

    def __sub__(self, other):
        try:
            return Fraction(
                (self.num * other.den - self.den * other.num), (self.den * other.den)
            )
        except AttributeError:
            return Fraction((self.num - self.den * other), (self.den))

    def __mul__(self, other):
        try:
            return Fraction(self.num * other.num, self.den * other.den)
        except AttributeError:
            return Fraction(self.num * other, self.den)

    def __truediv__(self, other):
        try:
            return Fraction(self.num * other.den, self.den * other.num)
        except AttributeError:
            return Fraction(self.num, self.den * other)

    def __pow__(self, other):
        return Fraction(self.num ** other, self.den ** other)

    def get_greatest(self, a, b):
        a = math.fabs(a)
        b = math.fabs(b)
        m = a * b
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return m // (a + b)


if __name__ == "__main__":
    fraction1 = Fraction(4, 5)
    print(fraction1 + Fraction(1, 8))
    print(Fraction(5, 7) / 10)
    print(Fraction(40, 70))
    print(Fraction(1, 6) + Fraction(1, 3))
    print(Fraction(1, 2) + Fraction(3, 4) + Fraction(1, 9) * Fraction(3, 5))