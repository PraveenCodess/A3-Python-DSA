# Write a Python program that takes a student's score as input and
# prints the corresponding grade. Use the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60


def grade(n):
    if n >= 90:
        print("A")
    elif n >= 80:
        print("B")
    elif n >= 70:
        print("C")
    elif n >= 60:
        print("D")
    else:
        print("F")


grade(69)
