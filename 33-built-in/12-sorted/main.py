# NOTE: Algorithm used for both is Timsort

numbers = [1, 21, 45, 5, 6, 6]
numbers.sort(reverse=True)  # * in-place

print(numbers)

print(sorted([1, 2, 6, 2, 4, 5, 8, 9], reverse=True))  # * new list


strings: list[str] = ["A", "b", "B", "C", "d", "E", "f"]
sorted_strings = sorted(strings, key=str.lower)
print(sorted_strings)


class Fruit:
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"


fruits: list[Fruit] = [
    Fruit("Apple", 70),
    Fruit("Apple", 50),
    Fruit("Banana", 100),
    Fruit("Ananas", 150),
]


def sort_by_calories(fruit: Fruit):
    return fruit.calories


sorted_fruits: list[Fruit] = sorted(fruits, key=sort_by_calories)
print(sorted_fruits)


def sort_by_names(fruit: Fruit):
    return fruit.name


sorted_fruits: list[Fruit] = sorted(fruits, key=sort_by_names)
print(sorted_fruits)

sorted_fruits: list[Fruit] = sorted(fruits, key=str)
print(sorted_fruits)
