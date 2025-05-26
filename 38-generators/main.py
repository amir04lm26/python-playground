def generate_list(num: int):
    for i in range(num):
        yield i


if __name__ == "__main__":
    generator = generate_list(10**100)
    # generator = generate_list(3)

    # print(next(generator))  # 0
    # print(next(generator))  # 1
    # print(next(generator))  # 2
    # print(next(generator))  # 3 #*  generate_list(3) -> throw StopIteration

    list_a: list[int] = []
    for number in generator:  # no error if reach the StopIteration
        if number == 100:
            break
        list_a.append(number)

    print(len(list_a))
    print(next(generator))  # the next in the list

    # generator comprehension
    yield_comprehension = (i for i in range(10**100))
    print(next(yield_comprehension))  # 0
    print(next(yield_comprehension))  # 1
    print(next(yield_comprehension))  # 2
    print(next(yield_comprehension))  # 4
