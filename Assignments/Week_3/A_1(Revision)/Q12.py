# Create a function that takes three arguments a, b, c and returns the
# sum of the numbers that are evenly divided by c from the range a, b
# inclusive.
# Examples:


def div(a, b, c):
    sum = 0
    for i in range(a, b + 1):
        if i % c == 0:
            sum += i
    return sum


a, b, c = map(int, input().split(","))
print(div(a, b, c))
