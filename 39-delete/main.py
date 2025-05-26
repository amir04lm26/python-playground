# first example
from dataclasses import dataclass


people: list[str] = ["Mario", "Toad"]

del people[1]

print(people)


# second example
data: dict[str, int] = {
    "field1": 100,
    "field2": 200,
}
del data["field1"]

print(data)


# third example
name: str = "Mario"

del name

# print(name) # NameError: name 'name' is not defined


# forth example
@dataclass
class Fruit:
    name: str
    calories: float


apple: Fruit = Fruit("Apple", 30)
print(apple)

del apple

# print(apple) # NameError: name 'apple' is not defined. Did you mean: 'tuple'?
