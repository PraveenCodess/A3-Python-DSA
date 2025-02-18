# Write a Python script that replaces each non-alphabetic character in a
# string with a space, using ASCII to determine character types.
# Input: "Hello, World!"
# Output: "Hello World "


def func(s):
    l = []
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90 or val >= 97 and val <= 122:
            l.append(i)
        else:
            val = " "
            l.append(val)
    print("".join(l))


s = "Hello, World!"
func(s)
