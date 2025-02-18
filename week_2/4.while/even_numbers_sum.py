def even_sum(s, e):
    sum = 0
    while s <= e:
        if s % 2 == 0:
            sum = sum + s
        s += 1
    print(sum)


s = int(input())
e = int(input())
even_sum(s, e)
