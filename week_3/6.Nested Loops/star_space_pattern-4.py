# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# for k in range(6 - 2, 0, -1):
#     for l in range(1, k + 1):
#         print("*", end=" ")
#     print()


# n = 9
# if n % 2 == 0:
#     addition = 1
# else:
#     addition = 2
# for i in range(1, n // 2 + addition):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# for i in range(n // 2, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()


n = int(input())
if n % 2 == 0:
    val = 1
else:
    val = 2
for i in range(1, n // 2 + val):  # +1+1
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for k in range(n // 2, 0, -1):
    for l in range(1, k + 1):
        print("*", end=" ")
    print()
