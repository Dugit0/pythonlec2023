from math import factorial
from decimal import Decimal
import decimal

def PiGen():
    decimal.getcontext().prec = 100000
    gen_ch = chudnovski()
    prev_num = str(Decimal(1) / next(gen_ch))
    next_num = str(Decimal(1) / next(gen_ch))
    i = 0
    while True:
        while prev_num[i] == next_num[i]:
            yield prev_num[i]
            i += 1
        prev_num = next_num
        next_num = str(Decimal(1) / next(gen_ch))

def chudnovski():
    cur = Decimal(0)
    k = 0
    while True:
        ch = Decimal((-1 if k % 2 else 1) * factorial(6*k) * (13591409 + 545140134*k))
        zn = Decimal(factorial(3*k) * factorial(k)**3 * (640320**3)**(k + 0.5))
        cur += 12 * (ch / zn)
        yield cur
        k += 1
pi_list = [c[0] for c in zip(PiGen(), range(1000))]
print(''.join(pi_list))
# a = chudnovski()
# print(a)
# print(type(next(a)))
# print(*(1 / c[0] for c in zip(chudnovski(), range(10))))

