# Write a Python program that computes the sum of the ASCII values of
# all characters in a string.
# Input: "abc"
# Output: 294 (sum of ASCII values for 'a', 'b', 'c')


def func(s):
    sum = 0
    for i in s:
        val = ord(i)
        sum += val
    print(sum)


s = "abc"
func(s)
