# for i in range(1, 6):
#     for j in range(1, 6 - i):
#         print(" ", end=" ")
#     for k in range(6 - i, 6):
#         print(k, end=" ")
#     print()


n = int(input())
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(i, n + 1):
        print(k, end=" ")
    print()
