class Smile:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        if self.n == 0:
            val = ""
        elif abs(self.n) == 1:
            val = '/1\\\n|"|\n\\-/'
        elif abs(self.n) > 1:
            rev = self.n < 0
            absn = abs(self.n)
            height = absn
            width = absn*2 - 1
            d = absn // 4
            first_row = f"/{str(absn)}{'-' * (width - len(str(absn)))}\\"
            matr = [f"|{' ' * width}|" for i in range(height)]
            matr[d] = f"|{' '*d}O{' '*(width - 2*(d + 1))}O{' '*d}|"
            matr[-d - 1] = f"|{' '*d} {'-'*(width - 2*(d + 1))} {' '*d}|"
            if rev:
                matr = matr[::-1]
            matr.insert(0, first_row)
            last_row = f"\\{'-' * width}/"
            matr.append(last_row)
            val = '\n'.join(matr)
        return val
    def __neg__(self):
        return Smile(-self.n)
    def __abs__(self):
        return abs(self.n)
    def __add__(self, other):
        return Smile(self.n + other.n)
    __radd__ = __add__
    def __sub__(self, other):
        return Smile(self.n - other.n)
    __rsub__ = __sub__
    def __mul__(self, other):
        return Smile(self.n * other)
    __rmul__ = __mul__

