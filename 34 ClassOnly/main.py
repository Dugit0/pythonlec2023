from itertools import product
class Struct:
    def __new__(cls):
        try:
            return cls.struct
        except:
            cls.struct = super(Struct, cls).__new__(cls)
            for i in map(lambda a: ''.join(a), product('abcd', repeat=4)):
                setattr(cls.struct.__class__, i, i)
            return cls.struct

a = Struct()
# print(dir(a))
print(a.__class__.__dict__)
