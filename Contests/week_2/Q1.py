# Create a function named as checkPrime that takes an integer as an
# argument. Print YES if the number passed is a prime number else print NO.


def checkprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
x = checkprime(n)
if x:
    print("Prime")
else:
    print("Not Prime")


# def checkPrime(num: int) -> None:
#     factors = 0
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             factors += 1
#         i += 1
#     if factors == 2:
#         print("Yes")
#     else:
#         print("No")


# checkPrime(7)
# checkPrime(8)
