# Write a program that takes two numbers as input and checks if the first
# number is divisible by the second.


def div(n1, n2):
    if n1 % n2 == 0:
        print("Divisible")
    else:
        print("Not Divisible")


div(25, 4)
