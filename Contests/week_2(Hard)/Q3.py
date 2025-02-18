# . Make a function named printWords which accepts an integer n from
# the user. Print the number as words.


def printWords(n):
    words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        0: "zero",
    }
    s = str(n)
    for i in s:
        if int(i) in words:
            print(words[int(i)], end=" ")


n = int(input())
printWords(n)


# def reverse(n):
#     res = 0
#     while n > 0:
#         l = n % 10
#         res = (res * 10) + l
#         n = n // 10
#     return res


# def printWords(n):
#     rev_num = reverse(n)
#     while rev_num > 0:
#         ld = rev_num % 10
#         if ld == 0:
#             print("Zero", end=" ")
#         elif ld == 1:
#             print("One", end=" ")
#         elif ld == 2:
#             print("Two", end=" ")
#         elif ld == 3:
#             print("Three", end=" ")
#         elif ld == 4:
#             print("Four", end=" ")
#         elif ld == 5:
#             print("Five", end=" ")
#         elif ld == 6:
#             print("Six", end=" ")
#         elif ld == 7:
#             print("Seven", end=" ")
#         elif ld == 8:
#             print("Eight", end=" ")
#         elif ld == 9:
#             print("Nine", end=" ")
#         rev_num = rev_num // 10


# n = int(input())
# printWords(n)
