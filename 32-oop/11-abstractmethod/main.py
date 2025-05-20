from abc import ABC, abstractmethod
# abc -> abstract base class


class Phone(ABC):
    def __init__(self, model: str):
        self.model = model

    @property
    @abstractmethod
    def power(self) -> int: ...  # ellipsis

    @abstractmethod
    def call_target(self, person: str): ...


class IBanana(Phone):
    def __init__(self, model: str):
        super().__init__(model)

    @property
    def power(self):
        return 89

    @property
    def made_in(self) -> str:
        raise NotImplementedError("This method is not yet implemented")

    def call_target(self, person: str):
        print(f"Calling {person} ...")


# phone = Phone(
#     "iBanana"
# )  # TypeError: Can't instantiate abstract class Phone with abstract methods call_target, power

phone = IBanana("ZS55")
phone.call_target("09398671414")
print(phone.power)
# print(phone.made_in) # NotImplementedError: This method is not yet implemented
