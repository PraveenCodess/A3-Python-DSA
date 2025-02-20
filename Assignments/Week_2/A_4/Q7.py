# Keep asking numbers from user until the user enters 0. Then display
# the average of all numbers.


# def avg():
#     n = int(input())
#     if n != 0:
#         global sum
#         global c
#         sum += n
#         c += 1
#         avg()
#     if n == 0:
#         print(sum / c)


# sum = 0
# c = 0
# avg()


n = int(input())
sum = 0
c = 0
while n != 0:
    sum += n
    c += 1
    n = int(input())
if n == 0:
    print(sum / c)
