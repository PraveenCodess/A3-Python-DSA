# Write a function named is_odd_even that determines if a number is
# odd or even without using the modulo operator (%). Hint: Use division or
# subtraction.


def is_odd_even(n):
    if (n // 2) * 2 == n:
        return "Even"
    else:
        return "Odd"


n = int(input())
print(is_odd_even(n))
