# Create a function that returns the thickness (in meters) of a piece of
# paper after folding it n number of times. The paper starts off with a
# thickness of 0.5mm.
# Examples:
# num_layers(1) ➞ "0.001m"
# # Paper folded once is 1mm (equal to 0.001m)
# num_layers(4) ➞ "0.008m"
# # Paper folded 4 times is 8mm (equal to 0.008m)
# num_layers(21) ➞ "1048.576m"
# # Paper folded 21 times is 1048576mm (equal to 1048.576m)
# There are 1000mm in a single meter.Don't round answers.


def thickness(n):
    return f"{(2**n) * 0.5 * (1 / 1000)}m"


n = int(input())
print(thickness(n))


# def num_layers(n):
#     final = 0.0005
#     for i in range(n):
#         final += final

#     return str(final) + "m"
