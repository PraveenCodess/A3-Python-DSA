# Create a function named factorial which takes a integer as an input and
# returns the factorial of that number.


def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)


factorial(5)
