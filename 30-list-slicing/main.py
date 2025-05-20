numbers: list[int] = list(range(21))

print(numbers)
print(numbers[::3])
print(numbers[10::3])
print(numbers[10:16:2])
print(numbers[10:])
print(numbers[:10])

print(numbers[:5] + numbers[5:])
