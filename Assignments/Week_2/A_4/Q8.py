# Write a function named pattern which accepts an integer n as an
# argument. Then print the following pattern.


def pattern(n):
    i = 1
    for i in range(1, n + 1):
        print(i * i, end=" ")


pattern(10)
