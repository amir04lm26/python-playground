# we can use any iterable type in the for-loop

people: list = ["Mario", "Luigi", "Peach", "Toad"]

for person in people:
    print(f"Hello, {person}")

numbers: range = range(0, 5)
for number in numbers:
    print(number)

for number in range(1, 4):
    print(number)

for number in range(3):
    print(number)

for char in "Mario":
    print(char)
