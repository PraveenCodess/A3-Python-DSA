def func(s):
    new_l = []
    w = s.split()
    for i in w:
        val = i[::-1]
        new_l.append(val)
    print(" ".join(new_l))


s = "python is good"
func(s)


# def reverseChar(string: str) -> str:
#     words = string.split()
#     return " ".join(i[::-1] for i in words)


# x = reverseChar("python is good")
# print(x)
