# pickling -> a process where a python object is converted into a byte stream
# unpickling -> do the opposite

import os
import pickle


text: str = "text"
number: int = 10

with open("54-pickling/save.txt", "w") as file:
    file.write(text + "\n")
    file.write(str(number) + "\n")


class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, ":", self.calories)


if __name__ == "__main__":
    # save the object with the same states (serializing the object)
    if not os.path.exists("54-pickling/save.pickle"):
        fruit: Fruit = Fruit("Banana", 100)

        fruit.calories = 150

        with open("54-pickling/save.pickle", "wb") as file:
            pickle.dump(fruit, file)
    else:
        with open("54-pickling/save.pickle", "rb") as file:
            fruit: Fruit = pickle.load(file)

        print(fruit.name, fruit.calories)
        fruit.describe_fruit()

        fruit.calories = 200
        fruit.describe_fruit()


# NOTE: Disclaim
"""
pickle data is unsecure and can not be trusted (not encrypted)
because it's just code and it will be run when we try to read it!
"""
