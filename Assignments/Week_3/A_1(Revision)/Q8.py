# Create a function that takes two arguments: the original price and the
# discount percentage as integers and returns the final price after the
# discount.
# Examples:
# dis(1500, 50) ➞ 750
# dis(89, 20) ➞ 71.2
# dis(100, 75) ➞ 25
# Your answer should be rounded to two decimal places.


def dis(p, d):
    return p - ((d / 100) * p)


p, d = map(int, input().split(","))
x = dis(p, d)
print(round(x, 2))
