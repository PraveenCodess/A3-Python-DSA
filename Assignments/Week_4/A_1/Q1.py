# Q1. Make a list of your own. Make two more empty list like odd and even.
# Put all the even numbers from original list to even and odd numbers to
# odd and print both lists. (Don’t remove anything from original one).

l = [1, 2, 3, 4, 5, 6]
l_e = []
l_o = []
for i in l:
    if i % 2 == 0:
        l_e.append(i)
    else:
        l_o.append(i)
print(l)
print(l_e)
print(l_o)
