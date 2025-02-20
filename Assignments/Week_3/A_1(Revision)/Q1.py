# Write a function that converts hours into seconds.
# Examples:
# 60 seconds in a minute, 60 minutes in an hour
# Don't forget to return your answer.


def h_to_s(n):
    return n * 60 * 60


n = int(input())
print(h_to_s(n))
