from dataclasses import dataclass


class Fruit:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories

    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__


@dataclass
class Fruit2:
    name: str
    calories: float = 2.9


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple", 10)
    apple2: Fruit = Fruit("Apple", 10)
    print(apple == apple2)  # True

    banana: Fruit = Fruit("Banana", 10)
    banana2: Fruit = Fruit("Banana", 10)
    print(banana == banana2)  # True #*  It is creating the equality check by default

    new_apple: Fruit = Fruit("Apple", 10)
    new_apple2: Fruit2 = Fruit2("Apple", 10)
    print(new_apple == new_apple2)  # True

    print(
        new_apple, new_apple2
    )  # <__main__.Fruit object at 0x104555350> Fruit2(name='Apple', calories=10)
