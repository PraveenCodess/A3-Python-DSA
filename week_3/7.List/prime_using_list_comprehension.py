def isPrime(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    return factors == 2


arr = [2, 5, 8, 10, 2, 7, 20, 30]
result = [i for i in arr if isPrime(i)]
print(result)
