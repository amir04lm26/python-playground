# loop through something that is infinite and the length is indefinite
a = 0

while a < 3:
    print("Hello", a)
    a += 1

print("Done")

for i in range(10):
    if i == 1:
        continue

    print(i)

    if i == 3:
        break

print("i", i)  # Output: 3
i = 0
while i < 10:
    i += 1
    if i == 2:
        continue

    print(i)

    if i == 3:
        break
