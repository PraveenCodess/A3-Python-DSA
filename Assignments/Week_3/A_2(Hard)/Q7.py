n = int(input())
if n % 2 == 0:
    val = 1
else:
    val = 2
for i in range(1, n // 2 + val):  # +1+1
    for j in range(n // 2, i - 1, -1):
        print(" ", end=" ")
    for k in range(1, i * 2 - 1 + 1):
        print(k, end=" ")
    print()
for i in range(n // 2, 0, -1):
    for j in range(0, n // 2 - i + 1):
        print(" ", end=" ")
    for k in range(1, i * 2 - 1 + 1):
        print(k, end=" ")
    print()
