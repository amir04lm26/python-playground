class Calculator:
    var: int = 22

    def __init__(self, name: str):
        self.name = name

    # instance method
    def description(self):
        print(f"{self.name} ia a calculator!")

    @staticmethod
    def add_numbers(*nums: float):
        total: float = 0
        for num in nums:
            total += num
        return total

    @classmethod
    def create_with_version(cls, name: str, version: int):
        print(cls.var)
        # return Calculator(f"{name}: ({version})")
        return cls(f"{name}: ({version})")


calc: Calculator = Calculator("Jeff")
calc.description()

print(Calculator.add_numbers(1, 2, 3, 4))
print(calc.add_numbers(1, 2, 3, 4))  # works in python

new_calc = Calculator.create_with_version("Bob", 100)
new_calc.description()
