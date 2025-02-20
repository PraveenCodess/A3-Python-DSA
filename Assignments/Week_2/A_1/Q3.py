# Attempt the same bill calculator question (Week 1 - Assignment 2 -
# Q5) but using function. Try calling function with different bill amount as a
# parameter and check the output.


def discount(n):
    if n >= 50000:
        print("30% Discount")
        dis = (30 / 100) * n
        print(n - dis)
    elif n >= 40000:
        print("25% Discount")
        dis = (25 / 100) * n
        print(n - dis)
    elif n >= 30000:
        print("20% Discount")
        dis = (20 / 100) * n
        print(n - dis)
    elif n >= 10000:
        print("10% Discount")
        dis = (10 / 100) * n
        print(n - dis)
    else:
        print("No Discount")


n = int(input())
discount(n)
