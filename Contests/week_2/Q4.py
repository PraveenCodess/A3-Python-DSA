# Make a function named factorial(), which takes an integer n. Return the
# factorial of that number.


def factorail(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)


n = int(input())
factorail(n)
