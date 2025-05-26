from functools import cache, wraps
import sys
from time import perf_counter
from typing import Any, Callable, OrderedDict, ParamSpec, TypeVar


P = ParamSpec("P")
T = TypeVar("T")


def memoize(func: Callable[P, T]) -> Callable[P, T]:
    cache: dict[str, T] = {}

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs):
        key: str = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


def memoize_opd(maxsize: int = 128):
    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        cache_dict: OrderedDict[Any, T] = OrderedDict()

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            try:
                key = (args, frozenset(kwargs.items()))
            except TypeError:
                # Fallback for unhashable args
                key = str(args) + str(kwargs)

            if key in cache_dict:
                cache_dict.move_to_end(key)
                return cache_dict[key]

            result = func(*args, **kwargs)
            cache_dict[key] = result
            if len(cache_dict) > maxsize:
                cache_dict.popitem(last=False)
            return result

        return wrapper

    return decorator


# @memoize
# @memoize_opd()
@cache  # cPython
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    sys.setrecursionlimit(10_000)
    start: float = perf_counter()
    # f: int = fibonacci(40)
    f: int = fibonacci(
        2000
    )  # with default limitation ->   RecursionError: maximum recursion depth exceeded while getting the str of an object
    end: float = perf_counter()

    print(f)
    print(f"Time: {end - start} seconds")
