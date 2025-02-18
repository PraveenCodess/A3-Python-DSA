# Create a function that takes the age in years and returns the age in
# days.
# Examples:
# Use 365 days as the length of a year for this challenge.
# Ignore leap years and days between last birthday and now.
# Expect only positive integer inputs.


def age(n):
    return 365 * n


n = int(input())
print(age(n))
