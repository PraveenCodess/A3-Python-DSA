# . Given a number, return a list containing the two halves of the number.
# If the number is odd, make the rightmost number higher.
# Examples
# number_split(4) ➞ [2, 2]
# number_split(10) ➞ [5, 5]
# number_split(11) ➞ [5, 6]
# number_split(-9) ➞ [-5, -4]
# All numbers will be integers.
# You can expect negative numbers too.


# n = int(input())
# l1 = []
# if n % 2 == 0:
#     e1 = n // 2
#     e2 = n - e1
#     l1.append(e1)
#     l1.append(e2)
# else:
#     e1 = n // 2
#     e2 = n - e1
#     l1.append(e1)
#     l1.append(e2)
# print(l1)


n = int(input())
l1 = []
e1 = n // 2
e2 = n - e1
l1.append(e1)
l1.append(e2)
print(l1)


# def number_split(n):
#     return [n // 2, n - n // 2]


# n = 4
# print(number_split(n))
