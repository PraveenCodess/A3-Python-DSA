# Write a python program to interchange first and last elements in a list


def func(l):
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    print(l)


l = [2, 4, 6, 8, 8, 5, 3, 4, 5, 7]
func(l)
