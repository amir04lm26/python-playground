import json
from typing import Any


# load json from file
with open("51-handling-json/sample.json", "r") as file:
    #     data: dict[str, Any] = json.load(file)
    #     print(data)

    pass

# with open("51-handling-json/sample.json", "r") as file:
#     data: str = file.read()
#     actual: dict[str, Any] = json.loads(data)
#     print(actual)


# load json from string
def get_json(path: str) -> dict[str, Any]:
    with open(path, "r") as file:
        data: str = file.read()
        actual: dict[str, Any] = json.loads(data)
        return actual


sample_data = get_json("51-handling-json/sample.json")
print(sample_data)


# create json from from a dict
sample: dict[str, Any] = {"name": "Elon", "age": 10, "has_mars": False}
sample_json = json.dumps(sample)
print(sample_json)

# create a json file from a dict
with open("51-handling-json/sample2.json", "w+") as file:
    sample: dict[str, Any] = {"name": "Elon", "age": 10, "has_mars": False}
    json.dump(sample, file)
    file.seek(0)
    print(file.read())
