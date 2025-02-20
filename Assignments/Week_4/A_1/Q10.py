# Ask 10 numbers from the user and put them into the list. Now remove
# all the even numbers from that list.


def func(l):
    l1 = []
    for i in l:
        if i % 2 != 0:
            l1.append(i)
    print(l1)


n = int(input())
l = []
for i in range(n):
    m = int(input())
    l.append(m)
func(l)
