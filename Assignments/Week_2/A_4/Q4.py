# Create a function named pattern which takes an integer as an input
# and print the following pattern.


def pattern(n):
    num = 10
    for i in range(n):
        print(num, end=" ")
        num += 10


pattern(11)
