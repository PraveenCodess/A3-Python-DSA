# . Create a function updateOddEven that accepts an List of Integers and
# update all the even numbers to 0 and update all the odd numbers to 1.


def updateOddEven(l):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = 0
        else:
            l[i] = 1
    print(l)


l = [34, 11, 91, 59, 33, 22]
updateOddEven(l)
