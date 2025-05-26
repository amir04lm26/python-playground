# #! In this case it's not clean
from typing import TypedDict


class InfoDict(TypedDict):
    text: str
    letters: int
    words: list[str]
    total_words: int
    avg_per_word: float


def get_info(text: str) -> InfoDict:
    return {
        "text": text,
        "letters": (length := len(text.replace(" ", ""))),
        "words": (words := text.split()),
        "total_words": (word_length := len(words)),
        "avg_per_word": round(length / word_length, 2),
    }


if __name__ == "__main__":
    for key, value in get_info("This is some text!").items():
        print(key, value, sep=": ")

    # second example
    while user_input := input("You: "):
        print(">>", user_input)

    print("We are done here...")
