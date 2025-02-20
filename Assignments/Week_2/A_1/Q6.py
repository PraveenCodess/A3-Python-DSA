# Write a function named is_even that takes a number as a parameter
# and prints "Even" if the number is even and "Odd" if the number is odd.


def is_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


n = int(input())
is_even(n)
