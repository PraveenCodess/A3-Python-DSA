# Write a function in Python that removes all numeric characters from a
# string by checking their ASCII codes.
# Input: "Abc123"
# Output: "Abc"


def func(s):
    l = []
    for i in s:
        val = ord(i)
        if val >= 48 and val <= 57:
            pass
        else:
            l.append(i)
    print("".join(l))


s = "Abc123"
func(s)
