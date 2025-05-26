from dataclasses import dataclass


status: int = 400

if status == 400:
    print("Bad Request")
elif status == 403:
    print("Forbidden Request")
elif status == 404:
    print("Not Found")
else:
    print("Something went wrong...")


match status:
    case 400:
        print("Bad Request")
    case 403:
        print("Forbidden Request")
    case 404:
        print("Not Found")
    case _:
        print("Something went wrong...")


# second example
if __name__ == "__main__":
    user_input: str = input("Command: ")
    p_command: list[str] = user_input.split()
    print(p_command)

    # pattern matching
    match p_command:  # can use objects here as well
        case ["find"]:  # if remove this the next find will match for `Command:  find`
            print("Finding default items!")
        case ["find", *images]:  # *images -> unpacked
            print(f"Finding {images}")
        case ["download", *images]:
            print("Downloading {images }")
        case ["remove" | "delete", *images] if (
            len(images) > 0  # will not recognize the command if the condition is no met
        ):  # pipeline in pattern matching
            print(f"Deleting {images}")
        case _:
            print("Invalid command, Try again!")

    # third example
    @dataclass
    class Animal:
        species: str
        sound: str
        age: int

    def describe(animal: Animal):
        match animal:
            case Animal(species="dog", sound="bark"):
                return "This is a dog that barks."
            case Animal(species="cat", sound="meow"):
                return "This is a cat that meows."
            case Animal(species=s, sound=snd):
                return f"This is a {s} that makes a {snd} sound."
            case _:
                return "Unknown animal."

    a1 = Animal("dog", "bark", 2)
    a2 = Animal("cat", "meow", 1)
    a3 = Animal("cow", "moo", 3)

    print(describe(a1))  # This is a dog that barks.
    print(describe(a2))  # This is a cat that meows.
    print(describe(a3))  # This is a cow that makes a moo sound.
