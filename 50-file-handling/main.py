# NOTE: File modes
"""
r read
a append
w write
x create (error if exists)

rt text mode
rb binary mode

a+ read & append
w+ read & overrides whole content
r+ read & override the content as needed
x+ create (error if exists) & read & write
"""

import os
import shutil


with open("./50-file-handling/sample.txt", "r") as file:
    # print(file.read())
    # print(file.read(10))  # Hello Worl
    # print(file.readline())

    t: list[str] = file.readlines()
    print(t)  # ['Hello World!\n', 'Second Line\n', 'End']


# with open("./50-file-handling/sample.txt", "w+") as file: # * overrides whole content
# with open("./50-file-handling/sample.txt", "r+") as file: # * start writing from the start of file, and override as needed
with open("./50-file-handling/sample.txt", "a+") as file:
    # file.write("\nThis is a new line.")
    file.write("")
    file.seek(0)  # to reset the pointer for reading from start
    print(file.read())


print()

with open("./50-file-handling/sample2.txt", "x+") as file:
    file.write("Some Text")
    file.seek(0)
    print(file.read())


# os.remove(
#     "./50-file-handling/sample3.txt"
# )  # FileNotFoundError: [Errno 2] No such file or directory: './50-file-handling/sample3.txt'


if os.path.exists("./50-file-handling/sample2.txt"):
    os.remove("./50-file-handling/sample2.txt")


# delete multiple files
folder = "50-file-handling/sample_folder"
for file in os.listdir(folder):
    path = f"{folder}/{file}"
    print("Deleting", path)
    # if os.path.exists(path):
    #     os.remove(path)


# remove empty directories
# os.rmdir(folder) # OSError: [Errno 66] Directory not empty: '50-file-handling/sample_folder'

# remove a folder and everything inside it
if os.path.exists(folder):
    # os.rmdir(folder)
    shutil.rmtree("50-file-handling/sample_folder")
