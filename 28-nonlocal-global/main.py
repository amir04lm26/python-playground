# x = 10  # This is not necessary


def func():
    global x  # to change the global x
    x = 20
    print("Inner", x)


func()
print("Outer", x)


def new_func():
    x = 10

    def inner_func():
        nonlocal x
        x = 30
        print("Other Inner", x)

    inner_func()
    print("Other Outer", x)


new_func()
