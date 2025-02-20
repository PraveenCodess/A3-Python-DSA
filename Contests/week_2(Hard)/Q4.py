# Make a function named checkArmstrong which accepts an integer n
# from the user. Return True or False if that number is an armstrong number


def checkArmstrong(n):
    sum = 0
    s = str(n)
    for i in range(len(s)):
        sum += int(s[i]) ** len(s)
    if sum == n:
        return True
    else:
        return False


n = int(input())
print(checkArmstrong(n))
