# n = int(input())
# for i in range(1, n // 2 + 1 + 1):
#     for j in range(1, (n // 2 + 1) - i + 1):
#         print(" ", end=" ")
#     for k in range(1, i * 2 - 1 + 1):
#         print(i, end=" ")
#     print()
# for l in range((n // 2 + 1) - 1, 0, -1):
#     for m in range((n // 2 + 1) - l):
#         print("@", end=" ")
# for n in range(1, (l * 2 - 1) + 1):
#     print(l, end=" ")
# print()


n = int(input())
if n % 2 == 0:
    val = 1
else:
    val = 2
for i in range(1, n // 2 + val):  # +1+1
    for j in range(1, (n // 2 + 1) - i + 1):
        print(" ", end=" ")
    for k in range(1, i * 2 - 1 + 1):
        print(i, end=" ")
    print()
for i in range((n // 2 + 1) - 1, 0, -1):
    for j in range((n // 2 + 1), i, -1):
        print(" ", end=" ")
    for k in range(1, (i * 2 - 1) + 1):
        print(i, end=" ")
    print()


# def pattern(n: int) -> None:
#     for i in range(1, n // 2 + 2):
#         for j in range(n // 2 - i + 1):
#             print(" ", end=" ")
#         for k in range(2 * i - 1):
#             print(i, end=" ")
#         print()
#     for i in range(n // 2, -1, -1):
#         for j in range(n // 2 - i + 1):
#             print(" ", end=" ")
#         for k in range(2 * i - 1):
#             print(i, end=" ")
#         print()


# pattern(9)
