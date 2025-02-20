# Calculate the factorial of a given number using a while loop.
# Example, n = 5
# 5 x 4 x 3 x 2 x 1
# Output: 120


def fact(n):
    mul = 1
    i = n
    while i > 0:
        mul = mul * i
        i = i - 1
    print(mul)


fact(5)
