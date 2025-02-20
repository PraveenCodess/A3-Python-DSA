n = int(input())
for i in range(n, 0, -1):
    for j in range(i):
        if j % 2 == 0:
            print(1, end=" ")
        else:
            print(2, end=" ")
    print()


# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             print(2, end=" ")
#         else:
#             print(1, end=" ")
#     print()
