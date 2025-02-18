# Ask a number from user n1. From 1 to n1, print how many prime
# numbers are there.


def prime(n):
    c = 0
    for i in range(2, n + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            c += 1
    print(c)


prime(10)
