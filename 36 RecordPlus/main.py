def Record(my_slots, **kwargs):
    def decor(cls):
        
        class NewClass(cls):
            from copy import copy
            __slots__ = sorted(list(set(copy(cls.__slots__)) | set(my_slots.split())))
            del copy
            
            def __init__(self):
                super().__init__()
                for key, value in kwargs.items():
                    setattr(self.__class__, key, value)

            def __iter__(self):
                return (i for i in sorted(filter(lambda a: not a.startswith('_'), dir(self))))

            def __str__(self):
                res = ""
                for i in self:
                    if i in self.__slots__:
                        try:
                            res += f"{i}={getattr(self, i)}|"
                        except AttributeError:
                            res += f"{i}|"
                    else:
                        res += f"{i}:{getattr(self, i)}|"
                return res[:-1]
            # def __next__(self):
            #     return 0
        
        return NewClass
    return decor




