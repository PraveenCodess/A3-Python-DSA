# Write a python program to ask a string from user. Then count the
# number of vowels and number of consonants in that string.
# (Make sure there are no spaces in string when you enter in terminal and also do
# not type any special characters except from alphabets)


# def func(s):
#     c_v = 0
#     c_c = 0
#     for i in s:
#         val = ord(i)
#         if val in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
#             c_v += 1
#         else:
#             c_c += 1
#     print(c_v)
#     print(c_c)


# s = "mewboi"
# func(s)


def func(s):
    c_v = 0
    c_c = 0
    for i in s:
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            c_v += 1
        else:
            c_c += 1
    print(c_v)
    print(c_c)


s = "mewboi"
func(s)
