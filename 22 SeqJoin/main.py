def joinseq(*seq):
    iters = [(i for i in j) for j in seq]
    buf = [next(iters[i], None) for i in range(len(seq))]
    while set(buf) != {None}:
        filt = list(filter(lambda a: a is not None, buf))
        min_el = min(filt)
        yield min_el
        min_ind = buf.index(min_el)
        buf[min_ind] = next(iters[min_ind], None)

