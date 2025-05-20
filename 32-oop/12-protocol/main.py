from typing import Protocol, runtime_checkable


# Protocol -> determine minimum requirements
"""
@runtime_checkable is a decorator from Python's typing module that allows you to use isinstance()
or issubclass() checks with a Protocol at runtime.
"""


@runtime_checkable  # not required
class Printable(Protocol):
    pages: int

    def print(self): ...

    def recycle(self): ...


class Book(Printable):
    pages: int
    edition: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        print("Printing book:", self.title)

    def recycle(self):
        print("Recycling book:", self.title)

    def burn(self):
        print(f"Burning the book({self.title})!")


class Magazine(Printable):
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print(self):
        print("Printing magazine:", self.title)

    def recycle(self):
        print("Recycling magazine:", self.title)


def print_item(printable: Printable):
    printable.print()


book: Printable = Book("Python")
print_item(book)

magazine: Printable = Magazine("Deluxe Magazine")
print_item(magazine)
