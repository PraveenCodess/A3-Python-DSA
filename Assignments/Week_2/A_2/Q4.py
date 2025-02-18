# Write a Python program that takes four numbers from the user.
# Implement a function to find the average of the first three numbers. Then,
# create another function to check if the average is greater than or equal to
# the fourth number. Make sure to use these two functions to determine and print
# whether the average is greater than or equal to the fourth number or not


def avg(n1, n2, n3):
    print(f"The average of {n1} , {n2} , {n3} is : {(n1+n2+n3)//3}")
    return (n1 + n2 + n3) // 3


def greater(x, n4):
    if x > n4:
        print(f"The average is greater than {n4}")
    else:
        print(f"The average is less than {n4}")


x = avg(2, 167, 6)
greater(x, 15)
