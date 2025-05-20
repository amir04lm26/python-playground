class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color

    # string representation
    def __str__(self):
        return f"{self.model} ({self.color})"

    # representation
    def __repr__(self):
        return f"Car(model={self.model}, color={self.color})"


if __name__ == "__main__":
    car: Car = Car("BMW", "Blue")
    # print(car)  # without str dunder method -> <__main__.Car object at 0x1021e0550> -> default value for __repr__
    print(car)  # BMW (Blue)
    print(car.__repr__())  # Car(model=BMW, color=Blue)
