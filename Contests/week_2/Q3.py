# Create a function named sumNum(), which takes 2 parameters as n1
# and n2. Calculate and return the sum of all the numbers divisible by and 2
# and 7 between n1 to n2. Also if the sum is 0, then return -1.


def sunNum(n1, n2):
    sum = 0
    for i in range(n1, n2 + 1):
        if i % 2 == 0 and i % 7 == 0:
            sum += i
    return sum


n1 = int(input())
n2 = int(input())
x = sunNum(n1, n2)
if x == 0:
    print(-1)
else:
    print(x)
