# Create a function findLargest that accepts an List of Integers and
# returns the largest number from the list.


# def findLargest(l1):
#     l1.sort()
#     return l1[-1]


# l1 = [34, 11, 91, 59, 33, 22]
# print(findLargest(l1))


def findLargest(l1):
    val = l1[0]
    for i in l1:
        if i > val:
            val = i
    return val


l1 = [34, 11, 91, 59, 33, 22]
print(findLargest(l1))
