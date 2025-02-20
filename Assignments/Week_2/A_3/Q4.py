# Print all odd numbers less than 15 using a while loop


def odd():
    i = 1
    while i < 15:
        if i % 2 != 0:
            print(i, end=" ")
        i += 1


odd()
