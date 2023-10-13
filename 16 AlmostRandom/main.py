import random
def divrandom(a, b, s, p):
    a, b = min(a, b), max(a, b)
    if a % p == 0 and (s % p == 0 or a + s > b):
        return 0
    while True:
        ans = random.choice(range(a, b + 1, s))
        if ans % p:
            return ans
