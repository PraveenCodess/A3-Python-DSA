# . Create a function findSmallest that accepts an List of Integers and
# returns the smallest number from the list.


# def findLargest(l1):
#     l1.sort()
#     return l1[0]


# l1 = [34, 11, 91, 59, 33, 22]
# print(findLargest(l1))


def findSmallest(l1):
    min = l1[0]
    for i in l1:
        if i < min:
            min = i
    return min


l1 = [34, 11, 91, 59, 33, 22]
print(findSmallest(l1))
