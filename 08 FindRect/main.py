# from pprint import pprint


matr = []

s = input()
if s == "":
    print(0)
    exit(0)

while s:
    matr.append('.' + s + '.')
    s = input()

m = len(matr[0])
matr.insert(0, '.' * m)
matr.append('.' * m)
n = len(matr)
ans = 0

# pprint(matr)

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if matr[i][j] == '#' and matr[i - 1][j] == '.' and matr[i - 1][j - 1] == '.' and matr[i][j - 1] == '.':
            ans += 1
            # pprint(matr)

print(ans)
