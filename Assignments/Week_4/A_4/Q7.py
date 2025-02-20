# Write a python program to ask a string from user. Then count the
# number of vowels and number of consonants in that string.
# (User can type anything including symbols, spaces or anything else)


def func(s):
    c_v = 0
    c_c = 0
    for i in s:
        val = ord(i)
        if val in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
            c_v += 1
        else:
            if val >= 65 and val <= 90 or val >= 97 and val <= 122:
                c_c += 1
    print(c_v)
    print(c_c)


s = "mejifsiugljwboi#$%^%$12   4"
func(s)
