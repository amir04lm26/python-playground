users = {}  # dict

users = {"user1": "Mario123", "user2": "Luigi456"}

print(users)  # Output: {'user1': 'Mario123', 'user2': 'Luigi456'}
print(len(users))  # Output: 2

# access items from a dictionary
user1 = users["user1"]
print(user1)  # Mario123

# accessing invalid key
# print(users["invalid_key"])  # Output: KeyError: 'invalid_key'

# access any key without error
user1 = users.get("user1")
print(user1)
print(users.get("invalid_key"))  # Output: None

# get keys
print(users.keys())  # Output: dict_keys(['user1', 'user2'])

# get values
print(users.values())  # Output: dict_values(['Mario123', 'Luigi456'])
print(list(users.values()))  # Output: ['Mario123', 'Luigi456']

# change a value
users["user1"] = "Toad789"
print(users["user1"])  # Output: Toad789

# retrieve all of the items
user_items = users.items()
# return all of the users a Tuple inside a Dictionary
print(user_items)  # Output: dict_items([('user1', 'Toad789'), ('user2', 'Luigi456')])
print(list(user_items))  # Output: [('user1', 'Toad789'), ('user2', 'Luigi456')]

# update a dictionary
users.update({"hello": "123"})
users.update([("world", "456")])
# Iterable[tuple[str, str]]
print(
    users
)  # Output: {'user1': 'Toad789', 'user2': 'Luigi456', 'hello': '123', 'world': '456'}

# delete an item
print(users.pop("world"))  # Output: 456
print(users)  # Output: {'user1': 'Toad789', 'user2': 'Luigi456', 'hello': '123'}

# delete the last item
print(users.popitem())  # Output: ('hello', '123')
print(users)  # Output: {'user1': 'Toad789', 'user2': 'Luigi456'}

# clear the dictionary
users.clear()
print(users)  # output: {}

# nested items
users = {
    "user1": "Mario123",
    "user2": "Luigi456",
    "items": {
        "apple": 10,
    },
}
print(
    users
)  # Output: {'user1': 'Mario123', 'user2': 'Luigi456', 'items': {'apple': 10}}

# get an item with a fallback
print(users.setdefault("user1", "There is no key!"))  # Output: Mario123
print(users.setdefault("invalid_key", "There is no key!"))  # Output: There is no key!
