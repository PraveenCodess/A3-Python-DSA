# Create a function that takes a base number and an exponent number
# and returns the calculation.
# calculate_exponent(5, 5) ➞ 3125
# calculate_exponent(10, 10) ➞ 10000000000
# calculate_exponent(3, 3) ➞ 27
# Examples:
# All test inputs will be positive integers.
# Don't forget to return the result.


def cal(b, e):
    return b**e


b, e = map(int, input().split())
print(cal(b, e))
