from collections import abc
import keyword


class FrozenJSON:
    """
    一个只读接口，使用属性表示法，访问JSON类对象
    """

    def __init__(self, mapping):
        self.__data = dict()
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value    


    def __getattr__(self, name):
        if hasattr(self.__data, name):
            print("111")
            return getattr(self.__data, name)
        else:
            print("222")
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            print('333')
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            print('444')
            return [cls.build(item) for item in obj]
        else:
            print('555')
            return obj
        