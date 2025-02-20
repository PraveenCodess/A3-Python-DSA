def summ(n1, n2):
    sum = 0
    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            sum += i
    print(sum)


summ(1, 10)
