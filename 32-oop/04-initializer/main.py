class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.color = color
        print(f"{self.model} ({self.color})")

    def drive(self):
        print(f"{self.model} is now driving.")


if __name__ == "__main__":
    car: Car = Car("BMW", "Black")
    car2: Car = Car("Ferrari", "Red")

    car.drive()
