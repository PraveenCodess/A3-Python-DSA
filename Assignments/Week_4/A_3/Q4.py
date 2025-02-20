# Create a function findSmallest that accepts an List of Integers and
# returns the smallest number from the list.


def findSmallest(l):
    s = l[0]
    for i in l:
        if i < s:
            s = i
    return s


l = [34, 11, 91, 59, 33, 22]
print(findSmallest(l))
