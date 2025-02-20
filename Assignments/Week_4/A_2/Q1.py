# Make your own list of numbers. Ask a start and end position from User.
# Print the list from start position to end position using Slicing.


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = int(input())
e = int(input())
res = l[s : e + 1]
print(res)
