# Boyer–Moore majority vote algorithm
a = eval(input())
count = 1
while (b := input()):
    b = eval(b)
    if a != b:
        count -= 1
        if count == 0:
            a = eval(input())
            count = 1
    else:
        count += 1

print(a)
