# Ask a string from user. Print the count of capital alphabets, small
# alphabets, spaces, digits and then symbols (whatever are left, count them
# in symbols).


def func(s):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90:
            c1 += 1
        elif val >= 97 and val <= 122:
            c2 += 1
        elif val == 32:
            c3 += 1
        elif val >= 48 and val <= 57:
            c4 += 1
        else:
            c5 += 1
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print(c5)


s = input()
func(s)
