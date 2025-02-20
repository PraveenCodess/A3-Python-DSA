# # Create a function sumCountOddEven that accepts an List of Integers and
#  calculate sum of even and odd numbers.


def sumCountOddEven(l1):
    s_even = 0
    s_odd = 0
    for i in l1:
        if i % 2 == 0:
            s_even += i
        else:
            s_odd += i
    print(f"even numbers sum {s_even}")
    print(f"odd numbers sum {s_odd}")


l1 = [34, 11, 91, 59, 33, 22]
sumCountOddEven(l1)
