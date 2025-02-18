# Create a function named as printPrimeFactors that takes an integer n
# as a argument and print all the prime factors of that number.
# Example if number = 20
# Then the factors of 20 are 1,2,5,10,20.
# So prime factors are 2,5 (this is the output)


def printPrimeFactors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            x = i
            is_prime = True
            if x <= 1:
                is_prime = False
            for j in range(2, int(x**0.5) + 1):
                if x % j == 0:
                    is_prime = False
            if is_prime:
                print(x, end=" ")


n = int(input())
printPrimeFactors(n)


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


# def printPrimeFactors(num: int) -> None:
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             if checkPrime(i):
#                 print(i, end=" ")
#         i += 1


# printPrimeFactors(20)
# printPrimeFactors(7)
# printPrimeFactors(72)
