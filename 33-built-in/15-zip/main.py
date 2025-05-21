people = ("Mario", "Luigi", "Toad", "Bowser")
numbers = (10, 20, 30)
letters = ("a", "b", "c", "d")

zipped = zip(people, numbers, letters)
# zipped = zip(people, numbers, letters, strict=True)  # error for mismatching length
print(list(zipped))  # [('Mario', 10, 'a'), ('Luigi', 20, 'b'), ('Toad', 30, 'c')]
