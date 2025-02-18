# 6. Write a program to remove the nth index element from a list using a
# function.


def func(l1, n):
    l1.pop(n)
    print(l1)


l = [34, 11, 91, 59, 33, 22]
n = 3
func(l, n)


# def func(l1, n):
#     l1.pop(n)


# l = [34, 11, 91, 59, 33, 22]
# n = 3
# func(l, n)
# print(l)
