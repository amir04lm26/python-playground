people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]

# ! don't edit list when looping through at the same time
for person in people:
    if person == "Luigi":
        people.remove("Luigi")  # ! huge mistake

    if person == "Peach":
        print("Hi from Peach!")

    print(person, "->", people)

print()

# * solution
people: list[str] = ["Mario", "Luigi", "Peach", "Toad"]
people2: list[str] = []

for person in people:
    print(person, "->", people2)

    if person == "Luigi":
        pass
    else:
        people2.append(person)

    if person == "Peach":
        print("Hi from Peach!")

print(people2)
