def even_count(s, e):
    count = 0
    while s <= e:
        if s % 2 == 0:
            count = count + 1
        s += 1
    print(count)


s = int(input())
e = int(input())
even_count(12, 16)


# """
# start
# end
# Print how many even numbers are there
# """

# def countEven(start, end):
#     i = start
#     count = 0
#     while i <= end:
#         if i % 2 == 0:
#             count = count + 1
#         i += 1
#     return count

# print(countEven(1, 22))
# print(f"Number of even numbers = {countEven(1, 22)}")
# x = countEven(45, 99)
# print(x)
