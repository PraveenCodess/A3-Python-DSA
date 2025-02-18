# Write a function which accepts a String as a parameter and return each
# word being in reverse.


def func(s):
    x = [i[::-1] for i in s.split()]
    print(" ".join(x))


s = "python is great"
func(s)
