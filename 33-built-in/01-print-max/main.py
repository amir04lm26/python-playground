numbers = [1, 2, 3, 4, 5]
print(max(numbers))

name = "Amir Hossein"
print(max(name))

print("String", "t", 1, 2, "hello")  # Output: String t 1 2 hello
print("String", "t", 1, 2, "hello", sep=",")  # Output: String,t,1,2,hello
print("String", "t", 1, 2, "hello", end=" [END]\n")  # Output: String t 1 2 hello [END]

with open("./33-built-in/01-print-max/doc.txt", "wt+") as file:
    print("This will be file content.", file=file)


# [Reading File] - Common mode values:
"""
Mode	Description
'r'	Read (default). File must exist.
'w'	Write. Creates a new file or truncates (overwrites) if it exists.
'a'	Append. Creates a new file if it doesn't exist, adds to the end if it does.
'x'	Create. Fails if file exists.
'b'	Binary mode (e.g., 'rb', 'wb'). Used for non-text files (images, etc).
't'	Text mode (default, e.g., 'rt', 'wt'). Used for text files.
'+'	Read and write mode (e.g., 'r+', 'w+').
"""
