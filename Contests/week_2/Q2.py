# Print all the prime numbers between 1 to 100


for i in range(1, 101):
    is_prime = True
    if i <= 1:
        is_prime = False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
    if is_prime:
        print(i)


# def checkPrime(num: int) -> bool:
#     factors = 0
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             factors += 1
#         i += 1
#     if factors == 2:
#         return True
#     else:
#         return False


# def printPrimeInRange(n1, n2):
#     for i in range(n1, n2 + 1):
#         if checkPrime(i) == True:
#             print(i, end=" ")


# printPrimeInRange(1, 100)
