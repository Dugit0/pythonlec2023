from itertools import islice
class Geom:
    @staticmethod
    def iter(b, q):
        i = b
        while True:
            yield i
            i *= q
    
    def __init__(self, b, q):
        self.b = b
        self.q = q
        self.iter = Geom.iter(b, q)
    
    def __iter__(self):
        return self.iter
    
    def __next__(self):
        return next(self.iter)
    
    def __getitem__(self, args):
        cur_iter = Geom.iter(self.b, self.q)
        if args is Ellipsis:
            return cur_iter

        if isinstance(args, tuple):
            if len(args) == 3:
                args = (args[0], args[2], None)
            elif args[0] is Ellipsis:
                args = (None, args[1], None)
            elif args[1] is Ellipsis:
                args = (args[0], None, None)
        else:
            args = (args.start, args.stop, args.step)

        if args[0] is args[1] is args[2] is None:
            return cur_iter
        if args[0] is args[1] is None and args[2] < 0:
            return None
        if args[2] is not None and args[2] < 0:
            args = (args[1], args[0], args[2])
            if args[0] is None:
                args = (0, args[1], args[2])
            return list(islice(cur_iter, args[0], args[1] + 1))[::args[2]]
        return islice(cur_iter, *args)



