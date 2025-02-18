n = int(input())
if n % 3 == 0 and n % 5 == 0:
    print("FOOBAR")
elif n % 5 == 0:
    print("BAR")
elif n % 3 == 0:
    print("FOO")
else:
    print("FOOFOOBARBAR")
