# Develop a Python script that counts how many letters are in a string by
# checking ASCII values.
# Input: "Year 2022!"
# Output: 4


def func(s):
    c = 0
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90 or val >= 97 and val <= 122:
            c += 1
    print(c)


s = "Year 2022!"
func(s)
