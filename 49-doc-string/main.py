import other


# NOTE: Reference: https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html


def get_length(item: str) -> int:
    """
    Returns the total length of a string (excluding spaces)

    :param str item: The item that you want to get the length for.
    :return: The length of the item as an int.
    :raises TypeError: If item is not a str.
    """

    if isinstance(item, str):
        processed: str = "".join(item.split())
        return len(processed)

    raise TypeError(f"{item} is not a str")


length: int = get_length("Hello, world")
print(length)
print(get_length.__doc__)
