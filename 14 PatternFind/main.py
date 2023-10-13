def my_cmp(a, b, code):
    return not (a == code or b == code) and (b == '@' or a == b)

def pref_func(s, code):
    n = len(s)
    arr = [0] * n
    for i in range(1, n):
        j = arr[i - 1]
        while j > 0 and not my_cmp(s[i], s[j], code):
            j = arr[j - 1]
        if my_cmp(s[i], s[j], code):
            j += 1
        arr[i] = j
    return arr

s = input()
template = input()

code = 0
while chr(code) in s or chr(code) in template:
    code += 1

pref_arr = pref_func(template + chr(code) + s, chr(code))
# print(code)
# print(pref_arr)
if len(template) in pref_arr:
    print(pref_arr.index(len(template)) - len(template) * 2)
else:
    print(-1)

