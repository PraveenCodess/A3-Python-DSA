# Make your own list. Write a Python program that takes an integer as an
# input, and make a new list containing the last n elements of the original list
# but in reverse order. Using slicing logic.


def func(l, n):
    res = l[-1 : -n - 1 : -1]
    print(res)


l = [10, -5, 8, 3, -1, -9, 7, 2]
n = int(input())
func(l, n)
