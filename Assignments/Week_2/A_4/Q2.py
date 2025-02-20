# From 1 to 2000, print all the LEAP YEARS, using WHILE loop.


def leap():
    i = 1
    c = 0
    while i <= 2000:
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            print(i)
        i += 1


leap()
