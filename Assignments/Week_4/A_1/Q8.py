# Take 10 integer inputs from user and store them in a list. Now, copy all
# the elements in another list but in reverse order.

n = int(input())
l = []
for i in range(n):
    m = int(input())
    l.append(m)
l1 = l
l1.reverse()
print(l1)


# n = int(input())
# l = []
# for i in range(n):
#     m = int(input())
#     l.append(m)
# print(l)
# l1 = []
# for i in range(len(l) - 1, -1, -1):
#     l1.append(l[i])
# print(l1)
