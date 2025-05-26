from functools import wraps
from time import perf_counter, sleep
from typing import Any, Callable, ParamSpec, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])
"""
A callable (i.e., a function, method, or anything you can call with ()).
... (ellipsis) means the callable can take any number and types of arguments.
Any means the callable can return any type.
"""


def get_time(func: F) -> F:
    """Times any function"""

    @wraps(func)  # to keep the function name and doc the same
    def wrapper(*args: Any, **kwargs: Any):
        start_time: float = perf_counter()
        func(*args, **kwargs)  # unpacking the args & kwargs
        end_time: float = perf_counter()

        total_time: float = round(end_time - start_time, 3)
        print("Time:", total_time, "seconds")

    return cast(F, wrapper)


@get_time
def do_something(param: Any):
    """Do something important"""
    sleep(1)
    print(param)


T = TypeVar("T")
P = ParamSpec("P")


def repeat(times: int) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """Repeat function call `times` amount of times and return the final result"""

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            value: T = func(*args, **kwargs)
            for _ in range(times - 1):
                value = func(*args, **kwargs)

            return value

        return wrapper

    return decorator


@repeat(2)
def say_hello():
    print("Hello")


@repeat(1)
def func2(a: int, b: int):
    print(a, b)


if __name__ == "__main__":
    do_something(2)
    print("__name__", do_something.__name__)  # __name__ do_something
    print("__doc__", do_something.__doc__)  # __doc__ Do something important

    say_hello()
    func2(1, 2)
