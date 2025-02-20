# Write a function which accepts a String and another string (which will
# be a single character) as a parameter. Join that string along with that
# character but in reverse.


def func(s1, s2):
    print(s2.join(s1.split()[::-1]))


s1 = input()
s2 = input()
func(s1, s2)
