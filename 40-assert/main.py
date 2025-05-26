from typing import Any


def start_program(data: dict[str, Any]):
    """This starts the program"""  # -> doc  string
    # use in development
    assert isinstance(data, dict), "Invalid JSON"
    assert data, "No data found..."

    print("Program loaded successfully!")


if __name__ == "__main__":
    # start_program("asd") # AssertionError: Invalid JSON
    # start_program({})  # AssertionError: No data found...
    start_program({"name": "Mario"})

    print(__debug__)  # True (False in production mode)


"""
    # python -O 40-assert/main.py -> Disable the debug mode
    # python -OO 40-assert/main.py -> Disable the debug mode & Exclude the docs strings

    # Result:
    def start_program(data: dict[str, Any]):
        print("Program loaded successfully!")
"""
