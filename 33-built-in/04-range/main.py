import sys

number: range = range(
    10
)  # create an object with the concept of this number (It's not use that  number immediately)

print(number)  # range(0, 10)
print(list(number))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(10**20))  # range(0, 100000000000000000000)
print(sys.getsizeof(range(10**20)))  # 48 (bytes)
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(-10, 0, 2)))  # [-10, -8, -6, -4, -2]
print(list(range(0, -10, -1)))  # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
