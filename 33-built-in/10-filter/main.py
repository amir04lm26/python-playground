from typing import Any, Union


people: list[Union[str, int]] = ["Mario", "Luigi", 10, "Toad", 20]


def is_str(element: Any):
    return isinstance(element, str)


# we can use list comprehension instead, but filter provides lazy loading (we don't need to load the entire object into memory)
# filter -> iterator
filtered_people = list(filter(is_str, people))
print(filtered_people)
