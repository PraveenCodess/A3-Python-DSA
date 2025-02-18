# To create new lists
# result = []
# for i in range(1, 11):
#     result.append(i + 5)
# print(result)

# start = 4
# end = 13
# result = [i for i in range(start, end + 1)]
# print(result)

# start = 1
# end = 10
# result = ["EVEN" if i % 2 == 0 else "ODD" for i in range(start, end + 1)]
# print(result)

result = [i for i in range(1, 11) if i % 2 == 0]
print(result)
