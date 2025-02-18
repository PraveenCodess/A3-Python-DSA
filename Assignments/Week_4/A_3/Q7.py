# Create a function calculatePrime that accepts an List of Integers and
# print all the prime numbers in that list.


# def calculatePrime(l):
#     for i in l:
#         factors = 0
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 factors += 1
#         if factors == 2:
#             print(i, end=" ")


# l = [34, 11, 91, 59, 33, 22]
# calculatePrime(l)


def calculatePrime(l):
    for i in l:
        is_prime = True
        if i <= 1:
            is_prime = False
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            print(i, end=" ")


l = [34, 11, 91, 59, 33, 22]
calculatePrime(l)
