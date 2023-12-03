from inspect import get_annotations
class positioned(type):
    @staticmethod
    def __new__(metacls, name, parents, attributes):
        def my_str(self):
            return ' '.join([f"{key}={getattr(self, key)}" for key in get_annotations(self.__class__).keys()])
        attributes['__str__'] = my_str
        attributes['__match_args__'] = tuple(attributes['__annotations__'].keys())
        return super().__new__(metacls, name, parents, attributes)
    def __call__(cls, *args):
        annot = get_annotations(cls)
        obj = super().__call__()
        for key, val in zip(annot.keys(), args):
            setattr(obj, key, val)
        return obj

