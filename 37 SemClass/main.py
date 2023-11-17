from collections import defaultdict
class Lock:
    @staticmethod
    def locked(cls):
        class CustomDesc():
            def __get__(self, obj, objtype=None):
                try:
                    obj._lock
                except AttributeError:
                    return None
                if obj._lock_dict[obj._lock] == 0:
                    obj._lock_dict[obj._lock] = id(obj)
                    return obj._lock
                elif obj._lock_dict[obj._lock] == id(obj):
                    return obj._lock
                return
            def __set__(self, obj, value):
                try:
                    if obj._lock_dict[obj._lock] == id(obj):
                        obj._lock_dict[obj._lock] = 0
                except AttributeError:
                    pass
                obj._lock = value
            def __delete__(self, obj):
                try:
                    if obj._lock_dict[obj._lock] == id(obj):
                        obj._lock_dict[obj._lock] = 0
                except AttributeError:
                    pass


        class NewCLass(cls):
            _lock_dict = defaultdict(int)
            lock = CustomDesc()
            def __del__(self):
                del self.lock
                try:
                    super().__del__(self)
                except AttributeError:
                    del self
        
        return NewCLass



