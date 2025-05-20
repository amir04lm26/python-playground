"""
In Python, variable access levels are by convention, not enforced by the language:
Prefix	    Access Level	    Intended Use
public	    No prefix	        Accessible from anywhere
protected	Single underscore	Meant for internal use or subclasses
private	    Double underscore	Name-mangled to prevent external access
"""


class Lamp:
    def __init__(self, name: str, model: int, color: str):
        self.name = name
        self.__model = model  # private
        self._color = color  # protected - only use in class and in inherited class

    def description(self):
        self.__self_maintenance()
        print(self.name, self.__model, self._color)

    # private method
    def __self_maintenance(self):
        print(self.name, "is fixing itself.")


class ElectricLamp(Lamp):
    def __init__(self, name: str, model: int, color: str):
        super().__init__(name, model, color)

    def do_something(self):
        print(self._color)


if __name__ == "__main__":
    lamp: Lamp = Lamp("Lamp", 1010, "light")
    lamp.description()

    # print(lamp.__model)  # AttributeError: 'Lamp' object has no attribute '__model'
    print(
        lamp._Lamp__model
    )  # 1010 #! Don't access private attributes aka fields and methods like this
    print(
        lamp._color
    )  # light #! Don't access protected attributes aka fields and methods like this

    el_lamp: ElectricLamp = ElectricLamp("EL Lamp", 1010, "blue")
    el_lamp.do_something()
