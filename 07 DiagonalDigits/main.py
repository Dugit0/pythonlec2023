m, n = eval(input())
if m == 0 or n == 0:
    exit(0)
matr = [[0] * m for i in range(n)]
num = 1

i = 0
j = 0

mod = 0

while i != n - 1 or j != m - 1:
    # while 1 <= i < n - 1 and 1 <= j < m - 1:
    #     print(f"in {i}, {j}, {mod}")
    #     matr[i][j] = num
    #     num = (num + 1) % 10
    #     if mod == 0:    # move down
    #         i += 1
    #         j -= 1
    #     else:           # move up
    #         i -= 1
    #         j += 1
    if mod == 0:    # move down
        while 0 <= i + 1 < n and 0 <= j - 1 < m:
            i += 1
            j -= 1
            # print(f"reg {i}, {j}, {mod}")
            matr[i][j] = num
            num = (num + 1) % 10
        if i + 1 < n:
            i += 1
        else:
            j += 1
        matr[i][j] = num
        num = (num + 1) % 10
        # print(f"cha {i}, {j}, {mod}")
        mod = 1
    else:           # move up
        while 0 <= i - 1 < n and 0 <= j + 1 < m:
            i -= 1
            j += 1
            # print(f"reg {i}, {j}, {mod}")
            matr[i][j] = num
            num = (num + 1) % 10
        if j + 1 < m:
            j += 1
        else:
            i += 1
        matr[i][j] = num
        num = (num + 1) % 10
        # print(f"cha {i}, {j}, {mod}")
        mod = 0

for i in range(n):
    print(*matr[i])




