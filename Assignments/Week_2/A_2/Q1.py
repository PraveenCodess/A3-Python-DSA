# Create a function that takes three numbers as parameters and returns
# the largest among them. Also if no arguments are passed, make sure the
# parameters take default value as None and return answer as -1.


def largest(n1=None, n2=None, n3=None) -> int:
    if n1 == None and n2 == None and n3 == None:
        return -1
    else:
        return max(n1, n2, n3)


x = largest(21, 32, 3)
print(x)
x = largest()
print(x)
