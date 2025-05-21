import math

var: str = "Global"


def hello():
    return "GLOBAL"


class Fruit:
    def __init__(self):
        print("GLOBAL")


print(
    globals()
)  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x104b65310>, '__spec__': None, '__annotations__': {'var': <class 'str'>}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/amirjz/Documents/projects/python-playground/33-built-in/05-globals/main.py', '__cached__': None, 'math': <module 'math' from '/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload/math.cpython-311-darwin.so'>, 'var': 'Global', 'hello': <function hello at 0x104b08680>, 'Fruit': <class '__main__.Fruit'>}
