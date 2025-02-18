# Create a function named printPattern that takes one integer (num) as
# an argument. Print from -num to num. Also keep in mind number passed as
# an argument can be negative or positive


def printPattern(n):
    if n > 0:
        i = -n
        while i <= n:
            print(i, end=" ")
            i += 1
    else:
        i = -n
        while n <= i:
            print(n, end=" ")
            n += 1


printPattern(-9)
