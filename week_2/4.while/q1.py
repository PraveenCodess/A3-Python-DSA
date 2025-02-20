def print_n(start, end):
    while start <= end:
        print(start, end=" ")
        start += 1
    print()


start = int(input())
end = int(input())
print_n(start, end)
