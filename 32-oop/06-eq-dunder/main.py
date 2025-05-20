class Fruit:
    global_count: int = 0

    def __init__(self, name: str, count: int):
        self.name = name
        self.count = count

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple", 10)
    apple2: Fruit = Fruit("Apple", 10)

    # print(apple == apple2) # without __eq__ -> False
    print(apple == apple2)  # with __eq__ -> True

    print(apple.__dict__)  # {'name': 'Apple', 'count': 10}
    print(
        Fruit.__dict__
    )  # {'__module__': '__main__', '__annotations__': {'global_count': <class 'int'>}, 'global_count': 0, '__init__': <function Fruit.__init__ at 0x100b307c0>, '__eq__': <function Fruit.__eq__ at 0x100b30900>, '__dict__': <attribute '__dict__' of 'Fruit' objects>, '__weakref__': <attribute '__weakref__' of 'Fruit' objects>, '__doc__': None, '__hash__': None}
