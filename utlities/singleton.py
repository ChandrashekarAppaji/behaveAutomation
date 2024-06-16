# utilities/singleton.py
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ObjectManager(metaclass=SingletonMeta):
    def __init__(self):
        self.prg_elements = None
