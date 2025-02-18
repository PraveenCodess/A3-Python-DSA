# Write a function in Python that counts the number of digits in a given
# string using ASCII codes.
# Input: "Room 101"
# Output: 3


def func(s):
    c = 0
    for i in s:
        if i.isdigit():
            c += 1
    print(c)


s = "Room 101"
func(s)
