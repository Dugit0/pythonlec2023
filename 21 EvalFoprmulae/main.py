def evalform(formula, *args):
    arr = [i if i.isalpha() else ' ' for i in formula]
    vars = sorted(list(set(''.join(arr).split())))
    my_locals = {vars[i]: args[i] for i in range(len(vars))}
    return eval(formula, my_locals)

