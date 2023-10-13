from fractions import Fraction
from decimal import Decimal
import decimal

decimal.getcontext().prec = decimal.MAX_PREC
x1, y1, x2, y2, x3, y3 = map(Decimal, input().split(','))
a1 = x2 - x1
a2 = y2 - y1
b1 = x3 - x1
b2 = y3 - y1
ans = abs((a1*b2 - a2*b1)) / 2
# num, den = map(Decimal, ans.as_integer_ratio())
# print(num / den)
print(ans)
