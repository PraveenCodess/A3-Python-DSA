n = int(input())
if n % 2 == 0:
    val = 1
else:
    val = 2
for i in range(n // 2 + 1, 0, -1):
    for j in range(i, n // 2 + val):  # +1+1
        print(j, end=" ")
    print()
for i in range(2, n // 2 + 1 + 1):
    for j in range(i, n // 2 + 1 + 1):
        print(j, end=" ")
    print()


# n = int(input())
# for i in range(n // 2 + 1, 0, -1):
#     for j in range(i, n // 2 + 1 + 1):
#         print(j, end=" ")
#     print()
# for i in range(2, n // 2 + 1 + 1):
#     for j in range(i, n // 2 + 1 + 1):
#         print(j, end=" ")
#     print()
