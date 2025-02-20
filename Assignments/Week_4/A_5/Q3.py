#  Implement a function in Python to check if a string is alphanumeric by
# examining the ASCII values of its characters.
# Input: "Var123"
# Output: True


def func(s):
    is_alpha = False
    is_numm = False
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90 or val >= 97 and val <= 122:
            is_alpha = True
        elif val >= 48 and val <= 57:
            is_numm = True
    if is_alpha and is_numm:
        print(True)
    else:
        print(False)


s = "Var123"
func(s)
