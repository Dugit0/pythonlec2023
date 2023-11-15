def Record(my_slots, **kwargs):
    def decor(cls):
        
        class NewClass(cls):
            from copy import copy
            __slots__ = sorted(list(set(copy(cls.__slots__)) | set(my_slots.split())))
            def __str__(self):
                res = ""
                for i in sorted(self.__slots__):
                    res += f"{i}|"
                return res[:-1]
            def __iter__(self):
                return 0
            def __next__(self):
                return 0
        
        return NewClass
    return decor





@Record("b c", d=11, e=12)
class C:
    __slots__ = ["a", "b"]
    c = 8
    d = 9

c = C()
c.a, c.c = 42, 100500
print(c, "//", "".join(c.__slots__))
print(*(getattr(c, attr, "<NOPE>") for attr in c))
for i, attr in enumerate(c):
    try:
        setattr(c, attr, i)
    except AttributeError:
        pass
print(c, "//", *(getattr(c, attr, "<NOPE>") for attr in c))





# def param_dec(my_len):
#     def decor(cls):
#         cls.__len__ = lambda self: my_len
#         return cls
#     return decor

# def param_dec(my_len):
#     def decor(cls):
#         class NewClass(cls):
#             def __len__(self):
#                 return my_len
#         return NewClass
#     return decor
#
# class A:
#     def __len__(self):
#         return 0
# a = A()
# print(len(a))
# b = param_dec(42)(A)()
# print(len(b))
# c = A()
# print(len(c))
