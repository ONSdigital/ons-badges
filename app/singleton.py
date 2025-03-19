import threading


class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton
    The reason for this being a metaclass is to ensure that the _instances of the class are NOT shared across all
    children of this class
    E.g if two separate classes inherit from this class, the _instances attribute will not be shared between the two
    classes whereas if this was simply a class, the _instances attribute would be shared between the two classes and
    cause unexpected behaviour

    So when inheriting from this class, ensure you inherit using the metaclass keyword eg.

    class MyClass(metaclass=SingletonMeta):
    """

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:  # Ensures thread safety
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
