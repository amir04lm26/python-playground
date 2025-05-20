class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Cat(Animal):
    def __init__(self, name: str, weight: int):
        super().__init__(name)  # super() -> using parent object

    def meow(self):
        print(f'{self.name} says "meow".')


class Dog(Animal):
    def __init__(self, name: str, job: str):
        super().__init__(name)
        self.job = job

    def work(self):
        print(f"{self.name} is working at {self.job}.")

    # * polymorphism
    def sleep(self):
        super().sleep()
        print(f"{self.name} is going to bed.")


if __name__ == "__main__":
    cat: Cat = Cat("Apple", 100)
    dog: Dog = Dog("Waffles", "Chef")

    cat.meow()
    cat.sleep()

    dog.work()
    dog.sleep()
