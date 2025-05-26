# NOTE: in most cases it's useful in combination with filter & map function


from typing import Callable


def square(a: float) -> float:
    return a**2


sq: Callable[[str], str] = lambda a: a**2

print(square(4))
print(sq(4))


# second example
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7]
even: list[int] = list(filter(lambda a: a % 2 == 0, numbers))
print(even)
