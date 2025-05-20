from typing import Self

# NOTE: __new__ vs __init__
"""
Method	    Purpose	                        When it Runs
__new__	    Creates a new instance	        Before __init__
__init__	Initializes an existing object	After __new__ returns it
"""

# NOTE: 🧱 __new__ – The Builder
"""
Purpose: Actually creates and returns a new instance of the class.

Called first, before __init__.

Used for:
Immutable types (e.g., str, int, tuple)
Custom instance creation (e.g., singleton patterns, metaclasses)

Must return the new object.
"""

# NOTE: 🔧 __init__ – The Initializer
"""
Purpose: Initializes the object that was just created.

Called after __new__

Used for:
Setting up instance attributes

Running any setup code
"""

# NOTE: 🧠 In summary:
"""
✅ __new__ builds the object → only used when you need control over object creation.
✅ __init__ runs every time an instance is created → used to set up the object.
"""


# singleton


class Connection:
    __instance = None

    # new is always called before the initializer
    def __new__(cls, *args, **kwargs) -> Self:  # type: ignore
        if cls.__instance is None:
            print("Connecting....")
            cls.__instance = super().__new__(
                cls
            )  # allocates and returns the new object instance
            return cls.__instance
        print("Warning: There's already a connection!")
        return cls.__instance

    # initializer
    def __init__(self):
        """
        Even though the object is the same (== True), __init__() still runs every time, because
        it's not suppressed.
        """
        if not hasattr(
            self, "_initialized"
        ):  # Without this line this snippet will run again and again in instantiation
            print("Connected to internet!")
            self._initialized = True


connection = Connection()
connection2 = Connection()
print(connection == connection2)  # Output: True


print()


# factory


class Vehicle:
    def __new__(cls, wheels: int):
        if wheels == 2:
            return Motorbike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)  # allocates and returns the new object instance

    # every args in new should be in initializer as well
    def __init__(self, wheels: int):
        self.wheels = wheels
        print(f"Initializing vehicle with {wheels} wheels")


class Motorbike:
    def __init__(self):
        print("Initializing motorbike")


class Car:
    def __init__(self):
        print("Initializing car")


car = Vehicle(4)
h2r = Vehicle(2)
truck = Vehicle(12)  # allocates and returns the new object instance
