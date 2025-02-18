# Create a function countOddEven that accepts an List of Integers and
# print how many even and odd numbers are there.


def countOddEven(l1):
    c_even = 0
    c_odd = 0
    for i in l1:
        if i % 2 == 0:
            c_even += 1
        else:
            c_odd += 1
    print(f"Total even numbers {c_even}")
    print(f"Total odd numbers {c_odd}")


l1 = [34, 11, 91, 59, 33, 22]
countOddEven(l1)
