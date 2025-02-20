# Write a program to check if number is divisible by 2 and 3 but not 8.


def div(n):
    if n % 2 == 0 and n % 3 == 0 and n % 8 != 0:
        print("Yes")
    else:
        print("No")


div(12)
