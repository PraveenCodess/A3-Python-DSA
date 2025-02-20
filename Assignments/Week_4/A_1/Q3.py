# Write a Python function that takes two lists and returns True if they
# have at least one common element.


def func(l1, l2):
    for i in l1:
        if i in l2:
            return True
    return False


l1 = [34, 11, 91, 59, 33, 22]
l2 = [78, 14, 23, 34]
print(func(l1, l2))
