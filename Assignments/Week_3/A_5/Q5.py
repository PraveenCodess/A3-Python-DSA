# Create a function that takes a list of positive and negative numbers.
# Return a list where the first element is the count of positive numbers and
# the second element is the sum of negative numbers.
# Examples
# sum_neg([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) ➞ [10, -65]
# # There are a total of 10 positive numbers.
# # The sum of all negative numbers equals -65.
# sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]
# sum_neg([91, -4, 80, -73, -28]) ➞ [2, -105]
# sum_neg([]) ➞ []
# If given an empty list, return an empty list: []
# 0 is not positive.


def func(l1):
    l = []
    c = 0
    s = 0
    for i in l1:
        if i > 0:
            c += 1
        else:
            s += i
    if c == 0 and s == 0:
        print(l)
    else:
        l.append(c)
        l.append(s)
        print(l)


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# l1 = []
func(l1)


# def sum_neg(nums):
#     p, n = 0, 0
#     if nums == []:
#         return []
#     else:
#         for i in nums:
#             if i > 0:
#                 p += 1
#             else:
#                 n += i
#         return [p, n]
