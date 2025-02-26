# Create a function that finds how many prime numbers there are, up to
# the given integer.
# prime_numbers(10) ➞ 4
# # 2, 3, 5 and 7
# prime_numbers(20) ➞ 8
# # 2, 3, 5, 7, 11, 13, 17 and 19
# prime_numbers(30) ➞ 10
# # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29


def prime(n):
    count = 0
    for i in range(1, n + 1):
        is_prime = True
        if i <= 1:
            is_prime = False
        else:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
        if is_prime == True:
            count += 1
    return count


n = int(input())
print(prime(n))
