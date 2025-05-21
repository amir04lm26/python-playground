from types import FunctionType


a: str = "a"


def do_something():
    pass


def b():
    pass


if __name__ == "__main__":
    print(callable(a))  # False
    print(callable(do_something))  # True
    print(callable(b))  # True
    print(type(do_something))  # <class 'function'>
    print(isinstance(do_something, FunctionType))  # True


# NOTE: Summary
"""
callable(obj) → True for any callable (functions, methods, classes with __call__)
isinstance(obj, types.FunctionType) → True only for regular functions.
"""
