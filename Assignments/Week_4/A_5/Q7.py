# Implement a Python function that checks if a string contains any
# special characters (non-alphanumeric) by using ASCII codes.
# Input: "password123!"
# Output: True


def func(s):
    is_spe = False
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90 or val >= 97 and val <= 122:
            pass
        elif val >= 48 and val <= 57:
            pass
        elif val == 32:
            pass
        else:
            is_spe = True
    return is_spe


s = "password123!"
print(func(s))
