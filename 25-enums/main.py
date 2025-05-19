from enum import Enum


class State(Enum):
    OFF = 0
    ON = 1


state = State.ON
print(state)

if state == State.ON:
    print("The lamp is turned on!")
    print(State.ON.name, State.ON.value)
elif state == State.OFF:
    print("The lamp is turned off!")


class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


def check_dolor(color: Color):
    print(color.value)


check_dolor(Color.GREEN)
