class Fruit:
    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple")
    banana: Fruit = Fruit("Banana")

    print(isinstance(apple, Fruit))
    print(isinstance(banana, Fruit))
    print(isinstance("string", str))
    print(isinstance(10, str))
    print(type(10))  # <class 'int'>
