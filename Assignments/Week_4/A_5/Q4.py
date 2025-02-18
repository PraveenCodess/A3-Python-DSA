# Write a Python function that toggles the case of each letter in a string
# (converts uppercase to lowercase and vice versa) using ASCII values.
# Input: "Python3.8"
# Output: "pYTHON3.8"


def func(s):
    l = []
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90:
            val = val + 32
            c = chr(val)
            l.append(c)
        elif val >= 97 and val <= 122:
            val = val - 32
            c = chr(val)
            l.append(c)
        else:
            l.append(i)
    print("".join(l))


s = "Python3.8"
func(s)
