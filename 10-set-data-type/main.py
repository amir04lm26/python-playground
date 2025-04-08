# sets are many memory efficient
# we can not insert duplicates in sets
items: set = {"Apple", "Banana", 10, True, "Apple", "banana"}

print(items)  # Output: ex.  {True, 'banana', 'Banana', 'Apple', 10}

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

# items[0] = "test" # TypeError: 'set' object does not support item assignment

print(len(items))

# create set from a tuple or list
print(set(("Banana", "Apple", "Banana")))  # Output: ex. {'Apple', 'Banana'}

# add items to a set
items.add("Orange")

# adding multiple elements - add any kind of list
items.update(["Carrot", 15])
# items.update(("Carrot", 15))

print(items)

# remove element from set
items.remove("Apple")
# items.remove("not_exists") # KeyError: 'apple'

print(items)

# discard
items.discard("not_exists ")  # does not throw an error

# pop or other array methods are unpredictable in operation
# ex. in pop we don't know which item is removed
#  items.pop()

# clear the set
items.clear()

print(items)  # Output: set()

# combining two sets
items: set = {"Apple", "Banana", "Apple", "banana"}
items2: set = {True, 10}

new_set: set = items.union(items2)
print(new_set)  # Output: ex. {True, 'banana', 10, 'Apple', 'Banana'}

new_set: set = items | items2
print(new_set)  # Output: ex. {True, 'banana', 10, 'Apple', 'Banana'}

items |= items2
print(new_set)  # Output: ex. {True, 'banana', 10, 'Apple', 'Banana'}

# to only keep the duplicates
items: set = {"Apple", "Banana", "Apple", "banana", True}
items2: set = {True, 10, "Banana"}

items.intersection_update(items2)
print(items)  # Output: ex. {True, 'Banana'}

# to only keep the duplicates - return a new set
items: set = {"Apple", "Banana", "Apple", "banana", True}
items2: set = {True, 10, "Banana"}

new_set = items.intersection(items2)
print(new_set)  # Output: ex. {True, 'Banana'}


# find the differences of sets
items: set = {"Apple", "Banana", "Apple", "banana", True}
items2: set = {True, 10, "Banana"}

items.symmetric_difference_update(items2)
print(items)  # Output: ex. {'Apple', 10, 'banana'}

# find the differences of sets - return a new set
items: set = {"Apple", "Banana", "Apple", "banana", True}
items2: set = {True, 10, "Banana"}

new_set = items.symmetric_difference(items2)
print(new_set)  # Output: ex. {'Apple', 10, 'banana'}


# create a empty set
people = set()
