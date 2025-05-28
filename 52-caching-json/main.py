import json
import requests


def fetch_data(*, update: bool = False, json_cache: str, url: str) -> list[object]:
    json_data = None

    if not update:
        try:
            with open(json_cache, "r") as file:
                json_data = json.load(file)
                print("Fetched data from the local cache!")
        except (FileNotFoundError, json.JSONDecodeError) as err:
            print(f"No local cache found {err}")
            json_data = None

    if not json_data:
        print("Fetching new json data... (Creating local cache)")
        json_data = requests.get(url).json()
        with open(json_cache, "w") as file:
            json.dump(json_data, file)

    return json_data


if __name__ == "__main__":
    api_url: str = "https://jsonplaceholder.typicode.com/comments"
    cache_file: str = "52-caching-json/comments.json"
    data = fetch_data(update=False, json_cache=cache_file, url=api_url)

    print(data[0])
