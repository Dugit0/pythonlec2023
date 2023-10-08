def func(n, s):
    if n == 1:
        print(s)
        return ""
    i = int(s.split("*")[-2]) if s else 2
    while i*i <= n:
        if n % i == 0:
            func(n // i, s + str(i) + "*")
        i += 1
    print(s + str(n))

a = int(input())
func(a, "")
