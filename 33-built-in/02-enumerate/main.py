names = ["Robert", "Mario", "Sofia", "James"]

for name in names:
    print(names.index(name) + 1, ":", name)

print()

# unpacking tuple while looping through
for i, name in enumerate(names, start=1):
    print(i, ":", name)
