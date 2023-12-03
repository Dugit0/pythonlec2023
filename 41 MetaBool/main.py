class empty(type):
    @staticmethod
    def __new__(metacls, name, parents, attributes):
        def my_bool(self):
            return all(self.__dict__.values())
        attributes['__bool__'] = my_bool
        return super().__new__(metacls, name, parents, attributes)


