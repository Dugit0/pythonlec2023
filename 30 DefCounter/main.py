import collections

class DefCounter(collections.Counter):
    def __init__(self, val=None, missing=-1):
        self.__missing = missing
        super().__init__(val)
    def __getitem__(self, key):
        if key in self.keys():
            return super().__getitem__(key)
        else:
            return self.__missing
    def __abs__(self):
        ans = 0
        for i in self:
            if self[i] > 0:
                ans += self[i]
        return ans


