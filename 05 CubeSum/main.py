n = int(input())
ans = 0

a = 1
while n - a**3 >= a**3:
    b3 = n - a**3
    i = int(b3**(1 / 3)) - 1
    while i**3 < b3:
        i += 1
    if i**3 == b3:
        ans += 1
    a += 1

print(ans)
