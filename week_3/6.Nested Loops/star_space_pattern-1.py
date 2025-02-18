# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end=" ")
#     for k in range(i, 0, -1):
#         print(k, end=" ")
#     print()


n = int(input())
for i in range(1, n + 1):
    for j in range(n, i, -1):
        print(" ", end=" ")
    for k in range(i, 0, -1):
        print(k, end=" ")
    print()
