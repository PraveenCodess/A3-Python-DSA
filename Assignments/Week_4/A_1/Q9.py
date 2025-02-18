# . Make a list. Write a simple program for addition of the 2nd element
# from start and 2nd element from the end.


def func(l1):
    sum = l1[1] + l1[-2]
    print(sum)


l1 = [1, 2, 3, 4, 5]
func(l1)
