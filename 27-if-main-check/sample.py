def do_something():
    print("Doing something...")


print(__name__)  # __main__ | sample
# Check if we're running current file directly
if __name__ == "__main__":
    do_something()
