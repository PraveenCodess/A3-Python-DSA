# a = [54, 65, 123, 433, 3, 54, 43, 12]
# print(a)
# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         a[i] = 0
#     else:
#         a[i] = 1
# print(a)


a = [54, 65, 123, 433, 3, 54, 43, 12]
print(a)
for i in range(len(a)):
    if i % 2 == 0:
        a[i] = 0
    else:
        a[i] = 1
print(a)
