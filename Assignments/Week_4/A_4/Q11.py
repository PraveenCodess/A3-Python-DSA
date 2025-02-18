# Ask a string from user. Print how many spaces are there in that string.


def func(s):
    c = 0
    for i in s:
        val = ord(i)
        if val == 32:
            c += 1
    print(c)


s = input()
func(s)
