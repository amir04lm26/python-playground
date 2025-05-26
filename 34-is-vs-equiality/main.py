import sys


class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__


if __name__ == "__main__":
    fruit_a: Fruit = Fruit("Banana", 10)
    fruit_b: Fruit = Fruit("Banana", 10)

    print(
        f"fruit_a id: {id(fruit_a)}, fruit_b id: {id(fruit_b)}"
    )  # ex. fruit_a id: 4378610768, fruit_b id: 4378611152
    print(sys.getsizeof(fruit_a), sys.getsizeof(fruit_b))  # 56 56
    print(f"fruit_a is fruit_b = {fruit_a is fruit_b}")  # False -> not the same object
    print(f"fruit_a == fruit_b = {fruit_a == fruit_b}")  # True

    # another example
    _ = 500
    a = _ + 500
    b = 1000

    print(a, b)
    print(f"a id: {id(a)}, b id: {id(b)}")
    print(f"a is b = {a is b}")  # False
    print(f"a == b = {a == b}")  # True

    # third example - python built-in optimization
    a = 10
    b = 10

    print(a, b)
    print(f"a id: {id(a)}, b id: {id(b)}")
    print(f"a is b = {a is b}")  # True
    print(f"a == b = {a == b}")  # True
