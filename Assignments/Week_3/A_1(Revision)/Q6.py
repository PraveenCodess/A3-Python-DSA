# Write a function that takes two integers (hours, minutes), converts
# them to seconds, and adds them.
# Examples:
# convert(1, 3) ➞ 3780
# convert(2, 0) ➞ 7200
# convert(0, 0) ➞ 0
# Don't forget to return the result.


def sec(h, m):
    return (h * 60 * 60) + (m * 60)


h, m = map(int, input().split(","))
print(sec(h, m))
