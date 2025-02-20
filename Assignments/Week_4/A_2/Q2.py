# Make your own list of numbers. Ask a start and end position from User.
# Make another different list which will contain number from start to end
# position. Use slicing logic.


l = [10, -5, 8, 3, -1, -9, 7, 2]
s = int(input())
e = int(input())
res = l[s : e + 1]
print(res)
