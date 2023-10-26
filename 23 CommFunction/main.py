from itertools import permutations

def checkcomm(fun, *args):
    ans = fun(*args)
    for i in permutations(args):
        if fun(*i) != ans:
            return False
    return True

