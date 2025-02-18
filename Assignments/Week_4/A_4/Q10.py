# Ask a string from user. Print how the count of alphabets (a-z or A-Z) in
# that string.


def func(s):
    c = 0
    for i in s:
        if i.isalpha():
            c += 1
    print(c)


s = input()
func(s)
