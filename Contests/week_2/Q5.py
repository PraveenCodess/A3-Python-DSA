# Make a function named sumPattern that takes an integer n as an
# argument from the user. And then calculate the sum of the following
# pattern.


def sumPattern(n):
    num = 1
    sum = 0
    for i in range(1, n + 1):
        x = 1
        if i <= 1:
            x = 1
        else:
            for j in range(1, i + 1):
                x *= j
        sum += 1 / x
    print(sum)


n = int(input())
sumPattern(n)
