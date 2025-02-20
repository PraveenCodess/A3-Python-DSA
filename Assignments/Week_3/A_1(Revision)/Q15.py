# Create a function that takes three values:
# h hours
# m minutes
# s seconds
# Return the value that's the longest duration.
# Examples:
# longest_time(1, 59, 3598) ➞ 1
# longest_time(2, 300, 15000) ➞ 300
# longest_time(15, 955, 59400) ➞ 59400
# No two durations will be the same.


def func(h, m, s):
    h1 = h * 60 * 60
    m1 = m * 60
    s1 = s
    x = max(h1, m1, s1)
    if x == s1:
        return s
    elif x == m1:
        return m
    else:
        return h


h, m, s = map(int, input().split(","))
print(func(h, m, s))


# def longest_time(h, m, s):
#     x = m // 60
#     y = s // 3600
#     if h > x and h > y:
#         return h
#     elif x > h and m > (s // 60):
#         return m
#     else:
#         return s


# h, m, s = map(int, input().split(","))
# print(longest_time(h, m, s))
