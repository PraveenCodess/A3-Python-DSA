# Ask x and n from user and then calculate the following answer.


def pattern(x, n):
    sum = 0
    num = 1
    for i in range(1, n + 1):
        sum += x**num
        if i == n:
            if n % 2 == 0:
                print(f" - {abs(x)}^{num}")
            else:
                print(f" + {x}^{num}")
        elif i == 1:
            print(f"{x}^{num}", end="")
        else:
            if i % 2 == 0:
                print(f" - {abs(x)}^{num} ", end="")
            else:
                print(f" + {abs(x)}^{num}", end="")
            ope = "-"
        num += 2
        x = -x

    print(sum)


x = int(input())
n = int(input())
pattern(x, n)


# def patterSum(x: int, n: int) -> float:
#     i: int = 1
#     total: float = 0
#     y: int = 1
#     while i <= n:
#         if i % 2 != 0:
#             total = total + (x**y)
#         else:
#             total = total - (x**y)
#         y += 2
#         i += 1
#     return total


# print(patterSum(6, 4))
# print(patterSum(9, 11))
