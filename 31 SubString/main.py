class SubString(str):
    def __sub__(self, other):
        ans = ""
        multiset = list(other)
        for i in self:
            if i in multiset:
                multiset.remove(i)
            else:
                ans += i
        return ans


