from time import perf_counter
import timeit


def time_func():
    start_time: float = perf_counter()

    for i in range(10**8):
        pass

    print("Hello")

    end_time: float = perf_counter()

    print(f"Total time: {end_time - start_time} seconds")


time_func()


# Second example
def make_calculation(first: int, second: int):
    for _ in range(10**3):
        pass

    return first + second


def do_something():
    for i in range(10):
        x: int = i**i


def get_time(func: str, repeat: int, number: int) -> float:
    """
    number=10000: Run the statement 10,000 times in a single repeat.
    repeat=5: Repeat that measurement 5 times, and return a list of the 5 timings (in seconds).
    """
    speed: float = min(
        timeit.repeat(
            func, repeat=repeat, number=number, globals=globals()
        )  # globals -> to access functions and variables
    )
    print(
        f"{func} --> {round(speed, 6)} sec (ran {repeat * number:,} times)"
    )  # * :, -> format string and add zero commas

    return speed


if __name__ == "__main__":
    get_time(
        "do_something()", repeat=10, number=10**5
    )  # do_something() --> 0.040456 sec (ran 1,000,000 times)

    a, b = 1, 2
    get_time("make_calculation(a, b)", repeat=10, number=10**5)

    get_time("x = [i for i in range(100)]", repeat=10, number=10**5)
