for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    for k in range(5 - i - 1):
        print(" ", end="")
    for l in range(5 - i - 1):
        print(" ", end="")
    for m in range(i + 1):
        print("*", end="")
    print()
