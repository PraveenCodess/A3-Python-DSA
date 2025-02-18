# Create a function countOddEven that accepts an List of Integers and
# print how many even and odd numbers are there.


def countOddEven(l1):
    c1 = 0
    c2 = 0
    for i in l:
        if i % 2 == 0:
            c1 += 1
        else:
            c2 += 1
    print(c1)
    print(c2)


l = [34, 11, 91, 59, 33, 22]
countOddEven(l)
