# # Make a function named reverse which accepts an integer n from the
# # user. Reverse the number passed as a parameter and return the reverse
# # number. Do not use STRINGS.


def reverse(n):
    while n > 0:
        l = n % 10
        print(l, end="")
        n = n // 10


n = int(input())
reverse(n)


# def rev(n):
#     s = str(n)
#     r = s[::-1]
#     print(r)


# n = int(input())
# rev(n)


# def reverse(num: int) -> int:
#     n = num  # Do not change the original parameter
#     result = 0
#     while n > 0:
#         last_digit = n % 10
#         result = (result * 10) + last_digit
#         n = n // 10
#     return result


# print(reverse(1000))
