for i in range(5):
    print(i, end=" ")
else:  # runs if everything in the for-loop executes successfully
    print("Success!")

for i in range(5):
    print(i, end=" ")

    if i == 2:
        break
else:  # if the loop is interrupted, this won't run
    print("Success!")

print("Done")

i = 0
while i < 4:
    print(i, end="")
    i += 1
else:  # this only executes if the condition turn into False
    print("Success!")

i = 0
while i < 4:
    print(i, end="")
    i += 1

    if i == 2:
        break
else:  # this only executes if the condition turn into False
    print("Success!")
