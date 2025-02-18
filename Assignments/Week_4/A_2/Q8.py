# Write a Python code to split a list into two halves using list slicing.
# (Keep the length of list even).


def func(l):
    n = len(l)
    m = n // 2
    l1 = l[0:m]
    l2 = l[m:n]
    print(l1)
    print(l2)


l = [2, 4, 6, 7, 8, 9, 6, 4, 3, 4, 5, 6, 7, 6]
func(l)
