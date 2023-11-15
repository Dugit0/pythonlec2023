from inspect import signature
def DefArgs(*constants):
    def decor(func):
        argc = len(signature(func).parameters)
        if len(constants) < argc:
            raise TypeError
        def my_func(*args):
            if len(args) > argc:
                raise TypeError
            args = list(args)
            for i in range(len(args), argc):
                args.append(constants[i])
            return func(*args)
        return my_func
    return decor




