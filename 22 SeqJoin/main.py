# def joinseq(*seq):
#     seq = [(i for i in seq[j]) for j in range(len(seq))]
#     buf = []
#     for i in seq:
#         cur = next(i, None)
#         if cur is not None:
#             buf.append(cur)
#     while len(buf) > 0:
#         min_val = min(buf)
#         yield min_val
#         min_ind = buf.index(min_val)
#         cur = next(seq[min_ind], None)
#         if cur is not None:
#             buf[min_ind] = cur

def joinseq(*seq):
    pass

    # yield from s

ans = joinseq("abs", "qr", "azt")
