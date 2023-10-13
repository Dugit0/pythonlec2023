n, m = eval(input())

max_width = len(f"{n}.*.{n}.=.{n*n}")
max_mul = len(str(n))
max_prod = len(str(n * n))
num_col = (m + 3) // (max_width + 3)
num_row = (n + num_col - 1) // num_col

cur_mul1 = 1
for row in range(num_row):
    print("=" * m)
    for cur_mul2 in range(1, n + 1):
        small_row = ""
        for col in range(num_col):
            if cur_mul1 + col > n:
                break
            small_row += str(cur_mul1 + col).rjust(max_mul, '.')
            small_row += ".*."
            small_row += str(cur_mul2).ljust(max_mul, '.')
            small_row += ".=."
            small_row += str((cur_mul1 + col) * cur_mul2).ljust(max_prod, '.')
            if col != num_col - 1 and cur_mul1 + col != n:
                small_row += ".|."
        print(small_row)
    cur_mul1 += num_col
print("=" * m)

