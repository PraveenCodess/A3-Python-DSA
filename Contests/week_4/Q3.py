# Python Program to remove all duplicates from a given string.

s = "helloworld"
l = []
for i in s:
    if i in l:
        pass
    else:
        l.append(i)
print("".join(l))
