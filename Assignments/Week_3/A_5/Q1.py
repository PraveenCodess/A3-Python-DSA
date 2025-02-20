# When resistors are connected together in series, the same current
# passes through each resistor in the chain and the total resistance, RT, of
# the circuit must be equal to the sum of all the individual resistors added
# together. That is:
# RT = R1 + R2 + R3 ...
# Create a function that takes an array of values resistance that are
# connected in series, and calculates the total resistance of the circuit in
# ohms. The ohm is the standard unit of electrical resistance in the
# International System of Units ( SI ).
# Examples
# series_resistance([1, 5, 6, 3]) ➞ "15 ohms"
# series_resistance([16, 3.5, 6]) ➞ "25.5 ohms"
# series_resistance([0.5, 0.5]) ➞ "1.0 ohm"


# def sum(l1):
#     sum = 0
#     for i in l1:
#         sum += i
#     return sum


# l1 = [float(n) if "." in n else int(n) for n in input().split(",")]
# x = sum(l1)
# if x > 1:
#     print(f"{x} ohms")
# else:
#     print(f"{x} ohm")


def sum(l1):
    sum = 0
    for i in l1:
        sum += i
    return sum


l1 = [1, 5, 6, 3]
x = sum(l1)
if x > 1:
    print(f"{x} ohms")
else:
    print(f"{x} ohm")


# def series_resistance(lst):
#     total = 0
#     for i in lst:
#         total += i
#     unit = "s" if total > 1 else ""
#     return "{} ohm{}".format(total, unit)


# lst = [0.5, 0.5]
# print(series_resistance(lst))
