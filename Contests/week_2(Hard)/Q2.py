# Make a function named checkPalindrome which accepts an integer n
# from the user. Return True or False if the number is palindrome or not.
# Palindrome means which is same as forward and backwards. Do not use
# STRINGS.


# def checkPalindrome(n):
#     s = ""
#     temp = n
#     while temp > 0:
#         l = temp % 10
#         s = s + str(l)
#         temp = temp // 10
#     if str(n) == s:
#         return True
#     else:
#         return False


# n = int(input())
# x = checkPalindrome(n)
# print(x)


def palindrome(n):
    res = 0
    while n > 0:
        l = n % 10
        res = (res * 10) + l
        n = n // 10
    return res


def checkPalindrome(n):
    reverse = palindrome(n)
    if reverse == n:
        return True
    else:
        return False


n = int(input())
print(checkPalindrome(n))
