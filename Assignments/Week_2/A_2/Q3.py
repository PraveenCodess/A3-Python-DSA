# Ask 3 numbers from user. Make a function which returns the middle of
# those 3 numbers. Then make a function to check if that middle number is
# divisible by both 3 and 4. Make 2 functions for reusability


def middle(n1, n2, n3):
    if n1 > n2 and n1 < n3 or n1 > n3 and n1 < n2:
        return n1
    elif n2 > n1 and n2 < n3 or n2 > n3 and n2 < n1:
        return n2
    elif n3 > n1 and n3 < n2 or n3 > n2 and n3 < n1:
        return n3


def check(x):
    if x % 3 == 0 and x % 4 == 0:
        print("Yes")
    else:
        print("No")


x = middle(12, 2, 18)
check(x)
