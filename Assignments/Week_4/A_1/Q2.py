# Write a function to remove duplicates from a list and print them.
def func(l1):
    l2 = []
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2


l = [9, 6, 2, 6, 1, 2, 2, 3, 3, 3, 4, 5, 4, 5, 6, 7, 5, 6, 7, 9, 7, 6, 9, 6, 4, 6]
print(func(l))
