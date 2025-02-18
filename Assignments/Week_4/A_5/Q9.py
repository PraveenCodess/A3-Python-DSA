# Develop a Python program that finds the character with the maximum
# ASCII value in a given string.
# Input: "hello"
# Output: 'o' (highest ASCII character in the string)


def func(s):
    max = 0
    for i in s:
        val = ord(i)
        if val > max:
            max = val
    print(chr(max))


s = "hello"
func(s)
