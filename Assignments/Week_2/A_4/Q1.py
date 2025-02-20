# Create a function named divs, which will take two parameters n1 and
# n2. Return the count of how many numbers from 1 to n1 are divisible by n2.


def divs(n1, n2):
    c = 0
    for i in range(1, n1 + 1):
        if i % n2 == 0:
            c += 1
    print(c)


divs(10, 2)
