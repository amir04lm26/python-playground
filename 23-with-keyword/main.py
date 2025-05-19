# file = open("./23-with-keyword/sample.txt")
# text = file.read()
# file.close()

# print(text)


# Better Approach - auto-close the file
with open("./23-with-keyword/sample.txt") as file:
    text = file.read()
    print(text)
