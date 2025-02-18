# Make your own list of numbers. Ask a start and end position from User.
# Make another dierent list which will contain number from start to end
# position. Use slicing logic. (Same as previous question), but now print the
# result in reverse:
# Example
# my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# Enter start position = 2
# Enter end position = 5
# Output: [-9, -1, 3, 8]


l = [10, -5, 8, 3, -1, -9, 7, 2]
s = int(input())
e = int(input())
res = l[e : s - 1 : -1]
print(res)


# l = [10, -5, 8, 3, -1, -9, 7, 2]
# s = int(input())
# e = int(input())
# res = l[s : e + 1]
# print(res[::-1])
