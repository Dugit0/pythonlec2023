from itertools import groupby
def LookSay():
    yield 1
    prev = '1'
    while True:
        cur = ""
        groups = [''.join(list(el)) for k, el in groupby(prev)]
        for i in groups:
            cur += str(len(i)) + i[0]
        yield from (int(i) for i in cur)
        prev = cur

