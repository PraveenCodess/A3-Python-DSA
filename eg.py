# n1 = int(input())
# n2 = int(input())
# l = []
# count = 0
# for i in range(n1, n2 + 1):
#     l.append(i)
# for i in l:
#     val = True
#     s = str(i)
#     emp = []
#     for j in s:
#         if j not in emp:
#             emp.append(j)
#         else:
#             val = False
#             break
#     if val:
#         count += 1
# print(count)


n = int(input())
lst = []
while n > 0:
    val1 = n % 10
    if val1 not in lst:
        lst.append(val1)
    n = n // 10
l = len(lst)
for i in range(-l, 0):
    print(lst[i], end="")
