# . A student will not be allowed to sit in exam if his/her attendance is less
# than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.

# 1. Print percentage of class attended
# 2. Print Is student is allowed to sit in exam or not.


def att(t, a):
    if ((a / t) * 100) >= 75:
        print("Allowed")
    else:
        print("Not Allowed")


att(87, 74)
