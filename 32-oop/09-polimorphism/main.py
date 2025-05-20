# NOTE: 1. Duck Typing (Informal Polymorphism)
"""
Python supports polymorphism through duck typing:

“If it walks like a duck and quacks like a duck, it’s a duck.”

No inheritance needed.

As long as the object implements speak(), it works.
"""


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


def animal_sound(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!

# NOTE: 2. Inheritance-Based Polymorphism
"""
Using base class references to call overridden methods of derived classes.

Even though we use a common interface (speak()), the behavior differs per subclass.
"""


class Animal:
    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


animals = [Dog(), Cat(), Animal()]

for animal in animals:
    print(animal.speak())
    """
    Woof!
    Meow!
    ...
    """


# NOTE: 3. Operator Overloading (Ad-hoc Polymorphism)
"""
Python allows you to define behavior for built-in operators using special methods.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1 + p2)  # (4, 6)


# NOTE: 💡 Summary
"""
Type	                Description
Duck                    Typing	Object's behavior matters, not its class
Inheritance-Based	    Common interface through base class or abstract class
Operator Overloading	Define custom behavior for operators (+, *, etc.)
"""
