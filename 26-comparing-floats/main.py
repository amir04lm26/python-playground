a = 0.3
b = 0.2 + 0.1

print(a == b, a, b)  # False 0.3 0.30000000000000004


def compare_floats(a: float, b: float, epsilon: float) -> bool:
    absolute = abs(a - b)
    print(f"{a} - {b} = {a - b}")
    return absolute <= epsilon


first = 0.8
second = 0.1 + 0.7
print(compare_floats(first, second, epsilon=1e-10))  # 0.0000000001
