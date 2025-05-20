class Lamp:
    def __init__(self, model: str, color: str):
        # * self.model -> attribute in python (field)
        self.model = model
        self.color = color

    def turn_on(self):
        print(self.model, "is turned on!")

    def turn_off(self):
        print(self.model, "is turned off!")

    def describe(self):
        print(f"Lamp: {self.model} ({self.color})")


red_lamp: Lamp = Lamp("RRX55", "Red")
red_lamp.turn_on()
red_lamp.turn_off()
red_lamp.describe()

red_lamp.color = "Blue"
red_lamp.describe()
print(red_lamp.model, red_lamp.color)


print()


blue_lamp: Lamp = Lamp("RRX05", "Blue")
blue_lamp.turn_on()
