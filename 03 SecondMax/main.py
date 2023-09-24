import sys

a = int(input())
while a != 0:
    new_a = int(input())
    if new_a == 0:
        print("NO")
        sys.exit(0)
    if a != new_a:
        b = new_a
        break
else:
    print("NO")
    sys.exit(0)

f_max = max(a, b)
s_max = min(a, b)

while (a := int(input())):
    if a > f_max:
        s_max = f_max
        f_max = a
    elif s_max < a < f_max:
        s_max = a

print(s_max)
