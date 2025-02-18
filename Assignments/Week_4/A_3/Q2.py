# Create a function sumCountOddEven that accepts an List of Integers
# and calculate sum of even and odd numbers.


def sumCountOddEven(l):
    s1 = 0
    s2 = 0
    for i in l:
        if i % 2 == 0:
            s1 += i
        else:
            s2 += i
    print(s1)
    print(s2)


l = [34, 11, 91, 59, 33, 22]
sumCountOddEven(l)
