a = 5

if a < 10:
    print("a < 10")
elif a == 10:
    print("a == 10")
else:
    print("a >= 10 || a == 10")

print("Done!")

# ternary operator equivalent
a = 5
print("Success!") if a > 2 else print("Failure")

a, b = 5, 10
print("a is greater") if a > b else print("b is greater")

result = a if a > b else b
print(result)  # Output: 10
