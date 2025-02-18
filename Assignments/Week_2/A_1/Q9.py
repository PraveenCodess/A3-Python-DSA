# Write a function named check_number that takes a number and prints
# whether it is positive, negative, or zero.


def check_number(n):
    if n == 0:
        print("Zero")
    elif n > 0:
        print("Pos")
    else:
        print("Neg")


n = int(input())
check_number(n)
