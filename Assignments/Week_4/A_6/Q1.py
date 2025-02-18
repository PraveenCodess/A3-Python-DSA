# Ask a string from user. If the length of string is odd, then change all the
# capital letters to small and vice versa, but if the length of string is even,
# reverse the string. Do this using a function and return the output.


def func(s):
    n = len(s)
    if n % 2 == 0:
        rev = s[::-1]
        return rev
    else:
        case = s.swapcase()
        return case


s = "AEroPLanes"
print(func(s))
