# input = input("Insert your maths: ")

input = """
10 * "hello "
"""

# 10 * 10 -> expression
# x = 10 -> statement 

result: float = eval(input)  # only accepts expressions
print(result)
