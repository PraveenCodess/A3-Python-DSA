# Write a function named calculate_interest that takes the principal,
# rate of interest, and time as parameters and prints the simple interest
# calculated.


def calculate_interest(p, r, t):
    si = p * t * r / 100
    print(si)


p = int(input())
r = int(input())
t = int(input())
calculate_interest(p, r, t)
