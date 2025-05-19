# name -> parameters
def greet(name: str):
    print(f"Hello, {name.capitalize()}")


# giving function an argument ("Mario" -> argument)
greet("Mario")


def do_something():
    for _ in range(3):
        print("Doing something")

    print("Done")


do_something()


# leave the default parameter at the end
def custom_greet(name: str, greeting: str = "Hello", age: int = 0):
    print(f"{greeting}, {name}! {age}")


custom_greet("Mario")
custom_greet("Mario", "Ciao")
custom_greet("Mario", age=23)
custom_greet(age=18, name="Mario")


def sum_numbers(a: float, b: float) -> float:
    return a + b


print(sum_numbers(10, 20), type(sum_numbers(10, 20)))  # Output: 30 <class 'int'>


# recursion
def do_something(n: int):
    print(n)

    if n <= 1:
        print("Done with function!")
        return

    do_something(n - 1)


do_something(5)


# * -> unlimited amount of arguments
def greet_people(*people: str, age: int):
    print(people, type(people), age)  # Output: ex. ('Mario', 'Luigi') <class 'tuple'> 10
    for name in people:
        print(f"Hello, {name}")


# age -> keyword argument
greet_people("Mario", "Luigi", age=10)


# keyword arguments
def do_something_new(
    *args,
    base: str,
    **kwargs,
):
    print(
        kwargs, type(kwargs)
    )  # Output: ex. {'name': 'Mario', 'age': 30, 'city': 'Texas'} <class 'dict'>
    print(kwargs["name"])  # Output: Mario
    print(args)  # Output: ex. ('hello',)
    print(base)


do_something_new("hello", name="Mario", age=30, city="Texas", base="named argument")


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, arg2, /):
    print(arg, arg2)


def kwd_only_arg(*, arg, arg2):
    print(arg, arg2)


def combined_example(pos_only, pos_only2, /, standard, *, kwd_only):
    print(pos_only, pos_only2, standard, kwd_only)


if __name__ == "__main__":
    standard_arg("ahh")

    # pos_only_arg(1, arg2=2)  # Output: ex. TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg2'
    pos_only_arg(1, 2)

    # kwd_only_arg(1, 2) # Output: ex. TypeError: kwd_only_arg() takes 0 positional arguments but 2 were given
    # kwd_only_arg(arg=1) # Output: ex. TypeError: kwd_only_arg() missing 1 required keyword-only argument: 'arg2'
    kwd_only_arg(arg=1, arg2=2)

    combined_example(1, 2, 3, kwd_only=4)
    combined_example(1, 2, standard=3, kwd_only=4)
