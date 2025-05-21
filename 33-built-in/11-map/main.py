numbers: list[int] = [1, 2, 3, 4, 5, 6]

# map -> iterator
str_numbers: list[str] = list(map(str, numbers))
print(str_numbers)
