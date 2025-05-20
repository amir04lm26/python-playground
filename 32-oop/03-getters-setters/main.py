class Fruit:
    # __ -> dunder methods or magic methods (double underscore)
    def __init__(self, name: str):
        self.__name = name  # * _ -> private variable (just a naming convention)

    @property  # property wrapper
    def name(self):
        print(f"{self.__name} is being accessed!")
        return self.__name

    @name.setter  # name -> property name
    def name(self, value: str):  # we can change the setter and getter name
        print(f"{self.__name} -> {value}!")
        self.__name = value


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple")
    print(apple.name)

    # without setter
    # apple.name = "banana" #! AttributeError: property 'name' of 'Fruit' object has no setter

    apple.name = "Orange"
    # print(apple.__name)  #! DO NOT USE THE PRIVATE VARIABLES DIRECTLY
    print(apple.name)
