# Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7)
# using function.


def minimum(n1, n2, n3, n4):
    print(min(n1, n2, n3, n4))


minimum(16.5, 5.64, 26.453, 8)


def salary(n):
    if n < 10000:
        inc = (5 / 100) * n
        print(n + inc)
    elif n <= 20000:
        inc = (10 / 100) * n
        print(n + inc)
    elif n <= 50000:
        inc = (15 / 100) * n
        print(n + inc)
    else:
        inc = (20 / 100) * n
        print(n + inc)


salary(50000)
