# Create a function findLargest that accepts an List of Integers and
# returns the largest number from the list.


# def findLargest(l):
#     lar = 0
#     for i in l:
#         if i > lar:
#             lar = i
#     return lar


# l = [34, 11, 91, 59, 33, 22]
# print(findLargest(l))


def findLargest(l):
    lar = l[0]
    for i in l:
        if i > lar:
            lar = i
    return lar


l = [34, 11, 91, 59, 33, 22]
print(findLargest(l))
