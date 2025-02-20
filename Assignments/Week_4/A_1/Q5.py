# Write a program to put all the common elements (in 2 lists) in another
# list and print it using function.


def func(l1, l2):
    l3 = []
    for i in l1:
        if i in l2:
            l3.append(i)
    print(l3)


l1 = [34, 11, 91, 59, 33, 22]
l2 = [11, 78, 14, 23, 34]
func(l1, l2)
