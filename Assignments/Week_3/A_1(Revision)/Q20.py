# Given an integer, create a function that returns the next prime. If the
# number is prime, return the number itself.
# Examples:
# next_prime(12) ➞ 13
# next_prime(24) ➞ 29
# next_prime(11) ➞ 11
# # 11 is a prime, so we return the number itself


def prime(n):
    is_prime = True
    if n <= 1:
        is_prime = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
    if is_prime:
        return n
    else:
        n += 1
        return prime(n)


n = int(input())
print(prime(n))
