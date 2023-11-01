class Smile:
    def __init__(self, n):
        self.n = n
        if n == 0:
            self.val = ""
        elif abs(n) == 1:
            self.val = '/1\\\n|"|\n\\-/'
        elif abs(n) > 1:
            rev = n < 0
            n = abs(n)
            height = n
            width = n*2 - 1
            d = n // 4
            first_row = f"/{str(n)}{'-' * (width - len(str(n)))}\\"
            matr = [f"|{' ' * width}|" for i in range(height)]
            matr[d] = f"|{' '*d}O{' '*(width - 2*(d + 1))}O{' '*d}|"
            matr[-d - 1] = f"|{' '*d} {'-'*(width - 2*(d + 1))} {' '*d}|"
            if rev:
                matr = matr[::-1]
            matr.insert(0, first_row)
            last_row = f"\\{'-' * width}/"
            matr.append(last_row)
            self.val = '\n'.join(matr)
    def __str__(self):
        return self.val
    def __neg__(self):
        return Smile(-self.n)
    def __abs__(self):
        return abs(self.n)
    def __add__(self, other):
        return Smile(self.n + other.n)
    __radd__ = __add__
    def __sub__(self, other):
        return Smile(self.n - other.n)
        pass
    __rsub__ = __sub__
    def __mul__(self, other):
        return Smile(self.n * other)
    __rmul__ = __mul__


