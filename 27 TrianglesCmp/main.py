from math import isclose
from functools import total_ordering

@total_ordering
class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
    def __bool__(self):
        eq1 = self.a < self.b + self.c
        eq2 = self.b < self.a + self.c
        eq3 = self.c < self.a + self.b
        pos = self.a > 0 and self.b > 0 and self.c > 0
        return pos and eq1 and eq2 and eq3
    def __abs__(self):
        if self:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c))**0.5
        else:
            return 0
    def __eq__(self, other):
        sort_self = sorted([self.a, self.b, self.c])
        sort_other = sorted([other.a, other.b, other.c])
        for i in zip(sort_self, sort_other):
            if not isclose(i[0], i[1]):
                return False
        return True
    def __lt__(self, other):
        return abs(self) < abs(other)
    def __str__(self):
        return f"{self.a}:{self.b}:{self.c}"


# tri = Triangle(3, 4, 5), Triangle(5, 4, 3), Triangle(7, 1, 1), Triangle(5, 5, 5), Triangle(7, 4, 4)
#
# for a, b in zip(tri[:-1], tri[1:]):
#     print(a if a else b)
#     print(f"{a}={abs(a):.2f} {b}={abs(b):.2f}")
#     print(a == b)
#     print(a >= b)
#     print(a < b)
