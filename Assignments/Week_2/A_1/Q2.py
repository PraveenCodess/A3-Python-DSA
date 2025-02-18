# Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but
# using function. Try calling function with different years as a parameter and
# check the output.


def leap(n):
    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print("Leap")
    else:
        print("Not Leap")


n = int(input())
leap(n)
