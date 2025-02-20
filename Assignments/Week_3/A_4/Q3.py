# Make a list of your own. Count how many numbers are divisible by 5.


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = 0
for i in l1:
    if i % 5 == 0:
        c += 1
print(c)
