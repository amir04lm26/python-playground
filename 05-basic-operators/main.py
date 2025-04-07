# arithmetic operators
print(1 + 2)
print(1 - 2)
print(1 * 2)
print(1 / 2)
print(1 / 0.5)  # Output: 4.0 - implicitly converted to float

# modulus operator
print(10 % 3)  # Output: 1

# exponential power
print(3**3)  # Output: 27

# floor division
print(10 // 3)  # Output: 3

a = 5
b = 10

# assignment operator
a = a + 3

# shorthand assignment operator
a += 3

b //= 3
print(b)  # Output: 3

# comparison operators | equality operator
print(10 == 5)  # Output: False
print(10 == 10)  # Output: True

# not equal operator
print(10 != 5)  # Output: True

# greater operator
print(10 > 5)  # Output: True

# smaller operator
print(10 < 5)  # Output: False

# greater than or equal to operator
print(10 >= 10)  # Output: True

# less than or equal to operator
print(10 <= 5)  # Output: False

# logical operators
print(a > b and b < 6)
print(a > b or b < 6)
print(not (a > b or b < 6))

# identity operators
a = 100.0
b = 1.0 * a

print(id(a))
print(id(b))
"""
the id() function returns the unique identity of an object. This identity is guaranteed to be unique and constant
for the object during its lifetime.

Think of id() as:
The memory address where the object is stored (at least conceptually).
"""

print(a is b)  # Output: False
print(a == b)  # Output: True
print(100.0 is 100.0)  # Output: True
"""
sometimes python stores variables in the same memory address event if we used two variable assignments 
"""

a = 42
b = a
print(id(a))  # e.g., 9788736
print(id(b))  # same as id(a), because b refers to the same object
print(a is b)  # Output: True

print(a is not b)  # Output: False

# membership operators
numbers = [1, 2, 3, 4, 5]

print(1 in numbers)  # Output: True
print(1 not in numbers)  # Output: False
