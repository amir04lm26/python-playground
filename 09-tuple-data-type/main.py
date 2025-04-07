# More memory efficient than lists
people: tuple = "Mario", "Luigi", "Peach"
people: tuple = ("Mario", "Luigi", "Peach")  # recommended
people: tuple[str] = ("Mario", "Luigi", "Peach")
people: tuple[str, ...] = ("Mario", "Luigi", "Peach")
people: tuple = ("Mario", "Luigi", "Peach", 2)


tp = ("Mario",)  # tuple
print(type(tp))  # Output: <class 'tuple'>

# people[0] = "Wa  rio"  # TypeError: 'tuple' object does not support item assignment

people: tuple = ("Mario", "Luigi", "Luigi")  # Output: ('Mario', 'Luigi', 'Luigi')

print(len(people))  # Output: 3

# create list from a tuple
people_list: list[str] = list(people)

# create tuple from a list
people_tuple: tuple = tuple(people_list)

# accessing element
print(people[0])  # Output: 'Mario'
print(people[-1])  # Output: 'Luigi'
print(people[1:3])  # Output: ('Luigi', 'Luigi')

print("Mario" in people)  # Output: True

# Append to a tuple by creating new one
print(people + ("Alex",))  # Output: ('Mario', 'Luigi', 'Luigi', 'Alex')

# Another way would be by converting to list, appending to it then reconvert it to tuple
people_tuple: tuple = tuple(people_list)
people_list.append("Mike")
print(tuple(people_list))  # Output: ('Mario', 'Luigi', 'Luigi', 'Mike')

# count a item in a list or tuple
print(people.count("Luigi"))  # Output: 2
print(people_list.count("Luigi"))  # Output: 2

print(people.count("luigi"))  # Output: 0

# find the index of an element
print(people.index("Luigi"))  # Output: 1
print(people_list.index("Luigi"))  # Output: 1

# unpacking tuples and lists
a, b, c = people
print(a, b, c)  # Output: Mario Luigi Luigi

# the items count should match
a, b, c, d = people_list
print(a, b, c, d)  # Output: Mario Luigi Luigi Mike

# using rest operator
a, *b = people
print(
    a, b, type(a), type(b)
)  # Output: Mario ['Luigi', 'Luigi'] <class 'str'> <class 'list'>

a, *b = people_list
print(a, b)  # Output: Mario ['Luigi', 'Luigi', 'Mike']
