# Create a python function named isPalindrome which accepts a string
# as a parameter and return True if its a palindrome. Palindrome are words
# which is same when read from start and same when read from the end.


def func(s1):
    s1 = s1.lower()
    if s1 == s1[::-1]:
        return True
    else:
        return False


s1 = input()
print(func(s1))
