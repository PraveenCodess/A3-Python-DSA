# Write a function which accepts a String as a parameter and return the
# reversed words as a String.


def func(s):
    print(" ".join(s.split()[::-1]))


s = "python is great"
func(s)
