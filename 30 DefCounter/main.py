import collections

class DefCounter(collections.Counter):
    def __init__(self, val=None, missing=-1):
        self.__keys = set()
        self.__missing = missing
        super().__init__(val)
    def __getitem__(self, key):
        if key in self.__keys:
            return super().__getitem__(key)
        else:
            return self.__missing
    def __setitem__(self, key, value):
        self.__keys.add(key)
        return super().__setitem__(key, value)
    def __delitem__(self, key):
        self.__keys.remove(key)
        return super().__delitem__(key)
    def __abs__(self):
        ans = 0
        for i in self:
            if self[i] > 0:
                ans += self[i]
        return ans


