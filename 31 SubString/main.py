from collections import UserString
class SubString(UserString):
    def __sub__(self, other):
        from collections import Counter
        ans = ""
        count = Counter(other)
        for i in self:
            if count[i] > 0:
                count[i] -= 1
            else:
                ans += i
        return ans
del UserString

