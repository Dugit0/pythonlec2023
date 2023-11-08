class Tester:
    def __init__(self, fun):
        self.__fun = fun
    def __call__(self, suite, allowed=[]):
        flag = 0
        for s in suite:
            try:
                self.__fun(*s)
            except Exception as ex:
                if type(ex) not in allowed:
                    return 1
                else:
                    flag = -1
        return flag


