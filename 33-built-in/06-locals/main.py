import math

var: str = "text"


def hello():
    hello_str: str = "str"
    hello_int: int = 0

    def inner():
        print(locals())  # {}

    inner()

    print(
        locals()
    )  # {'hello_str': 'str', 'hello_int': 0, 'inner': <function hello.<locals>.inner at 0x1002f8900>}


hello()
print(locals() == globals())  # True
