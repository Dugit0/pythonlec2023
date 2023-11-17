class A:
    def __delete__(self):
        return super().__delete__(self)
    def __del__(self):
        return super().__del__(self)

a = A()
