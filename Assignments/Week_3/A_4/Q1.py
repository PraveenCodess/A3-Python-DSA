# Make a list of your own. Print the whole list in reverse using FOR loop
# and WHILE loop


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l = len(l1)

for i in range(l - 1, -1, -1):
    print(l1[i], end=" ")

# l = len(l1) - 1
# while l >= 0:
#     print(l1[l], end=" ")
#     l -= 1
