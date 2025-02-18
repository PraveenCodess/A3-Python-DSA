# Create a function that takes two parameters and, if both parameters
# are strings, add them as if they were integers or if the two parameters are
# integers, concatenate them.
# stupid_addition(1, 2) ➞ "12"
# stupid_addition("1", "2") ➞ 3
# stupid_addition("1", 2) ➞ None
# If the two parameters are different data types, return None.
# All parameters will either be strings or integers.


from typing import Union


def func(a, b):
    if type(a) == int and type(b) == int:
        print(str(a) + str(b))
    elif type(a) == str and type(b) == str:
        print(int(a) + int(b))
    else:
        print("None")


a = int(input())
b = int(input())
func(a, b)
