n1 = input()
n2 = input()


def func(n1, n2):
    n1 = n1.lower()
    n2 = n2.lower()
    bool = True
    if len(n1) != len(n2):
        return False
    for i in n1:
        if n1.count(i) != n2.count(i):
            return False
    return True


print(func(n1, n2))
