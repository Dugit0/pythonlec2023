from itertools import product
my_prog = "class Struct:\n    __slots__ = []\n    " + "\n    ".join([f"{i} = '{i}'" for i in map(lambda a: ''.join(a), product('abcd', repeat=4))])
with open("out.py", "w") as f_out:
    print(my_prog, file=f_out)
eval(my_prog, globals())
# eval("""
# class A:
#     pass
#      """.strip(), globals())
# a = Struct()


