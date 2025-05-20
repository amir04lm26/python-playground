sample_list = []

for i in range(10):
    if i % 2 == 0:
        sample_list.append(i * 2)

print(sample_list)

# [result for element in list]
# sample_list2 = [i for i in range(10)]
# sample_list2 = [i for i in range(10) if i % 2 == 0]
sample_list2 = [i * 2 for i in range(10) if i % 2 == 0]

print(sample_list2)

people: list[str] = ["Mario", "Luigi", "Peach"]
cap_people = [person.upper() for person in people]
# cap_people = [person.upper() for person in ["Mario", "Luigi", "Peach"]]

print(people, cap_people)
