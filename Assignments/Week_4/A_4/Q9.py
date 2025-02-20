# Write a python program to only print second half of the string. Ask
# string from user.
# Example string: aeroplane
# Output: lane
# Example string: delhi
# Output: hi
# Example string: pavbhaji
# Output: aji


def func(s):
    n = len(s)
    val = n // 2
    print(s[val + 1 :])


s = input()
func(s)
