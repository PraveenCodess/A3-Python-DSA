# Don’t create a function, just print the following pattern
# 1 11 111 1111 11111....n times (Ask n from user)


n = int(input())
num = "1"
for i in range(n):
    print(int(num), end=" ")
    num = num + "1"
