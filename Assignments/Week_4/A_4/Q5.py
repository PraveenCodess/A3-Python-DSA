#  Write a Python program to check if a string has at least one letter and
# one number. If it has at least one letter and one number then print YES else
# print NO.


def func(s):
    is_alpha = False
    is_num = False
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 97 or val >= 97 and val <= 122:
            is_alpha = True
        if val >= 48 and val <= 57:
            is_num = True
    if is_alpha and is_num:
        return True
    else:
        return False


s = "12m3"
print(func(s))


# def checkNumberAndLetter(my_string: str) -> bool:
#     isLetter = False
#     isNumber = False

#     # Method 1
#     """
#     for ch in my_string:
#         if ch.isdigit():
#             isNumber = True
#         elif ch.isalpha():
#             isLetter = True

#     return isLetter and isNumber
#     """

#     for ch in my_string:
#         ascii_code = ord(ch)
#         if ascii_code >= 48 and ascii_code <= 57:
#             isNumber = True
#         elif (ascii_code >= 65 and ascii_code <= 90) or (
#             ascii_code >= 97 or ascii_code <= 122
#         ):
#             isLetter = True

#     return isLetter and isNumber


# print(checkNumberAndLetter("abc#$#1d"))
