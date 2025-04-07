greeting = "Hello "

print(greeting + "Mario")
print(greeting + "Luigi")

# snake_case
# case sensitive
happy_thoughts = "Happy"

# constants
# we must not  change the value of constants
PI = 3.1415

# string
text = "text"  # str

# numeric types
number = 100  # integer
number2 = -100  # integer
decimal = 0.5  # float
com = 8j  # complex

# sequence types
people = ["Mario", "Luigi"]  # list[str]
lotto_numbers = (1, 2, 3, 4, 5, 6)  # tuple
"""
A tuple in Python is a immutable ordered collection of elements.
Once you create a tuple, you cannot change, add, or remove elements from it
You have to create a new tuple if you want something else
"""
numbers = range(1, 1000)  # range (Output: 1 to 999)

# mapping type
users = {"user1": "Mario123", "user2": "luigi2022"}  # dictionary

# set
unique_numbers = {1, 2, 2, 3, 3, 5}  # set[int] (Output: 1235)
"""
Unlike lists or tuples, sets do not allow duplicates and do not maintain any specific order
They are particularly useful when you need to store values but don't care about their order
or need to remove duplicates from a collection.

Although sets are unordered, they are mutable — meaning you can add or remove elements.
However, the elements themselves must be immutable (e.g., numbers, strings, tuples).

For example:
``` python
valid_set = {(1, 2), (3, 4)}  # Tuples are immutable, so this works.
invalid_set = {[1, 2], [3, 4]}  # Lists are mutable, so this raises a TypeError.
```
"""

unique_numbers2 = frozenset({1, 2, 2, 3, 3, 5})  # frozenset[int]
"""
We can not edit frozen sets
"""

# boolean
connected = True  # bool

# bytes
ascii_vals = bytes([65, 66, 67])  # bytes - List of ASCII values (Output: b'ABC')
"""
A bytes object is an immutable sequence of bytes. Once created, the contents of the bytes object cannot be modified.
"""
hello_byte = b"hello"

# bytearray (Mutable)
byte_arr = bytearray("hello", "utf-8")  # bytearray
"""
A bytearray is a mutable sequence of bytes. Unlike bytes, you can modify the contents of a bytearray object.
"""
byte_arr2 = bytearray([65, 66, 67])

# memoryview
mv = memoryview(byte_arr2)  # memoryview
"""
A memoryview object in Python is a view of a given object that exposes the object's buffer interface. It allows you to access
the underlying memory of objects like bytes, bytearray, array, and other buffer-compatible objects without copying the data.
This can be highly efficient when working with large datasets since it allows you to manipulate or read data without
duplicating it in memory.

Key Benefits of memoryview:
Efficient memory usage: It provides a view on the underlying data, meaning no data is copied, making operations more efficient.

Supports slicing: You can slice the data in a memoryview without copying the data.

Shared memory: Multiple memoryview objects can refer to the same underlying memory block, which is useful in scenarios where
data needs to be accessed by multiple consumers.

Creating a memoryview
A memoryview is created by calling memoryview() on any object that supports the buffer protocol.
Common objects that support the buffer protocol are bytes, bytearray, array, and numpy arrays.
``` python
b = b"hello world"
mv = memoryview(b)

# View the underlying memory
print(mv)  # Output: <memory at 0x7ff7f6b5f240>
print(mv[0])  # Output: 104 (ASCII for 'h')
```

Example: Using memoryview with Files

# Open a binary file
``` python
with open("large_file.bin", "rb") as file:
    data = file.read(1024)  # Read the first 1024 bytes
    
    # Create a memoryview to avoid copying data
    mv = memoryview(data)
    
    # Work with the data efficiently
    print(mv[0:10])  # Access first 10 bytes without copying
```
"""

# empty
is_empty = None  # None
