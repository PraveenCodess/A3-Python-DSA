# Ask a positive number from user. Print all the numbers from positive
# number to 1.
# Example n = 7
# Output: 7 6 5 4 3 2 1


def num(n):
    i = n
    while i > 0:
        print(i, end=" ")
        i -= 1


n = int(input())
num(n)
