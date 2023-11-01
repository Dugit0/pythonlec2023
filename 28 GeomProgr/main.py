from itertools import tee, islice
class Geom:
    def __init__(self, b, q):
        def iter(b, q):
            i = b
            while True:
                yield i
                i *= q
        self.iter = iter(b, q)
        self.sec_iter = iter(b, q)
    
    def __iter__(self):
        return self.iter
    
    def __next__(self):
        return next(self.iter)
    
    def __getitem__(self, slice):
        self.sec_iter, buf = tee(self.sec_iter)
        if slice is Ellipsis:
            return buf
        if isinstance(slice, tuple) and slice[1] is Ellipsis:
            return islice(buf, slice[0], slice[2])
        if slice.start is None and slice.stop is None and slice.step < 0:
            return None
        if slice.step is not None and slice.step < 0:
            stop = slice.stop
            if stop is None:
                stop = 0
            return (i for i in [next(buf) for j in range(stop, slice.start + 1)][::slice.step])
        return islice(buf, slice.start, slice.stop, slice.step)


