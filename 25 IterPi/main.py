from decimal import Decimal
import decimal


def PiGen():
    decimal.getcontext().prec = 1101
    gen_ch = chudnovski()
    prev_num = str(1 / next(gen_ch))
    next_num = str(1 / next(gen_ch))
    i = 0
    while True:
        # print(f"{prev_num[:30]}\n{next_num[:30]}")
        while i < len(prev_num) and prev_num[i] == next_num[i]:
            yield next_num[i]
            i += 1
        # print("Not eq")
        prev_num = next_num
        next_num = str(1 / next(gen_ch))

def chudnovski():
    arr_factorial = [1]
    def factorial(n):
        nonlocal arr_factorial
        if n >= len(arr_factorial):
            for i in range(len(arr_factorial), n + 1):
                arr_factorial.append(arr_factorial[-1] * i)
        return arr_factorial[n]
                
    # cur = Decimal(0)
    cur = 0
    k = 0
    big_constant = 262537412640768000**Decimal('0.5')
    while True:
        ch = (-1 if k % 2 == 1 else 1) * factorial(6*k) * (13591409 + 545140134*k)
        zn = factorial(3*k) * factorial(k)**3 * big_constant
        cur += 12 * (ch / zn)
        yield cur
        k += 1
        big_constant *= 262537412640768000




# with open('real_ans.txt') as f_inp:
#     pi_str = f_inp.read()
#
# n = 1000
# pi = PiGen()
# my_ans = ""
# for i in range(n):
#     if pi_str[i] != (cur := next(pi)):
#         print(f"i = {i}\nmy = {cur}\nreal = {pi_str[i]}")
#         print(my_ans + cur)
#         print(pi_str[:i+1])
#         break
#     my_ans += cur


# pi_list = [c[0] for c in zip(PiGen(), range(10000))]
# print(''.join(pi_list))
# decimal.getcontext().prec = 100
# a = chudnovski()
# for i in zip(chudnovski(), range(10)):
#     print(1 / i[0])
# print(a)
# print(type(next(a)))
# print(*(1 / c[0] for c in zip(chudnovski(), range(10))))

