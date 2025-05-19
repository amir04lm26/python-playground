print(bool(""))  # Output: False
print(bool("anything"))  # Output: True
print(bool([]))  # Output: False
print(bool(()))  # Output: False
print(bool(set()))  # Output: False
print(bool(range(0)))  # Output: False
print(bool(0))  # Output: False
print(bool(0.0))  # Output: False
print(bool(complex(0j)))  # Output: False
print(bool(None))  # Output: False

var = ""
# var = None

# Output: Empty
if var:
    print(var)
else:
    print("Empty")
