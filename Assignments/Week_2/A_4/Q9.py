# . Ask a number from user. Print if that number is prime or not, use
# functions.


def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
x = prime(n)
if x:
    print("Prime")
else:
    print("Not Prime")
