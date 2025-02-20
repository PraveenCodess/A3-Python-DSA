# Create a function named calSum() which takes 2 integers n1 and n2 as a
# argument. Calculate the sum of all the numbers from n1 and n2 and
# RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
# then return “n1 should be smaller”.


def calsum(n1, n2):
    if n1 > n2:
        print("n1 should be samller")
    else:
        i = n1
        sum = 0
        while i <= n2:
            sum += i
            i += 1
        print(sum)


calsum(7, 3)
