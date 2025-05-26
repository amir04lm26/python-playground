import requests


def get(url: str):
    return "<TEST_RESPONSE>"


# monkey patching
requests.get = get


data = requests.get("https://google.com")
print(data)
