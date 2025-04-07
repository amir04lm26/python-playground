people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
multiTypeList: list = ["Mario", "Luigi", "Peach", "Toad", 10, True]

duplicated_people: list[str] = ["Mario", "Luigi", "Peach", "Peach", "Toad"]

print(people)
print(len(people))
print(people[0])  # Output: Mario
# print(people[4])  # Output: IndexError: list index out of range

print(people[-1])  # Output: Toad
print(people[0:2])  # Output: ['Mario', 'Luigi']
print(people[:2])  # Output: ['Mario', 'Luigi']
print(people[0:4])  # Output: ['Mario', 'Luigi', 'Peach', 'Toad']
print(people[0:])  # Output: ['Mario', 'Luigi', 'Peach', 'Toad']
print(people[-3:-1])  # Output: ['Luigi', 'P each']
print(people[-1:-3])  # Output: []
print(people[0:5])  # Output: ['Mario', 'Luigi', 'Peach', 'Toad']

print("Luigi" in people)  # Output: True
print("luigi" in people)  # Output: False

people[0] = "Shy Guy"
print(people)  # Output: ['Shy Guy', 'Luigi', 'Peach', 'Toad']

people[0:2] = ["Shy Guy", "Bowser"]
print(people)  # Output: ['Shy Guy', 'Bowser', 'Peach', 'Toad']

people.insert(2, "!!!")
print(people)  # Output: ['Shy Guy', 'Bowser', '!!!', 'Peach', 'Toad']

people.append("Alex")
print(people)  # Output: ['Shy Guy', 'Bowser', '!!!', 'Peach', 'Toad', 'Alex']


people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
people2: list[str] = ["Sonic", "Tails"]

new_list = people + people2
print(new_list)  # Output: ['Mario', 'Luigi', 'Peach', 'Toad', 'Sonic', 'Tails']
# people += people2 # Output: ['Mario', 'Luigi', 'Peach', 'Toad', 'Sonic', 'Tails']

people.extend(people2)
print(people)  # Output: ['Mario', 'Luigi', 'Peach', 'Toad', 'Sonic', 'Tails']


people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
people.remove("Peach")
# people.remove("peach") # ValueError: list.remove(x): x not in list
print(people)  # Output: ['Mario', 'Luigi', 'Toad']

# delete by index or the last one
people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
people.pop(2)
print(people)  # Output: ['Mario', 'Luigi', 'Toad']
people.pop()
print(people)  # Output: ['Mario', 'Luigi']

# reverse the list
people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
people.reverse()
print(people)  # Output: ['Toad', 'Peach', 'Luigi', 'Mario']

# sort the list
people.sort()  # sort the list alphabetically
print(people)  # Output: ['Toad', 'Peach', 'Luigi', 'Mario']

# clear the list
people.clear()
print(people)  # Output: []
