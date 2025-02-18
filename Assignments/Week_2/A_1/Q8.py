# Create a function named simple_calculator that takes three
# parameters: two numbers and an operation (addition or subtraction
# represented by '+' or '-'), and prints the result of the operation.


def simple_calculator(n1, n2, ope):
    if ope == "+":
        print(n1 + n2)
    elif ope == "-":
        print(n1 - n2)


n1 = int(input())
n2 = int(input())
ope = input()
simple_calculator(n1, n2, ope)
