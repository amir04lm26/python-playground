# with open("main.py") as f:
#     pass


class File:
    def __init__(self, name: str):
        self.name = name

    # what runs as soon as we open the file (with File)
    def __enter__(self):
        print(f"Opening {self.name}...")
        return self

    # this run when we're done with the with block
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        exc_type -> exception type
        exc_val  -> exception value
        exc_tb   -> exception traceback
        """
        print(f"Closing {self.name}...")


with File("main.py") as file:
    print(file.name)

print("Done!")
