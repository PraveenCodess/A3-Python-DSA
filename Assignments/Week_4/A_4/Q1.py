# Write a Python program to get the 4th element from the last element
# of a tuple.


t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
n = int(input())
if len(t) < n:
    print("Not enough elements")
else:
    print(t[-n])


# from typing import Tuple


# def fourthElementFromLast(tup: Tuple) -> None:
#     if len(tup) < 4:
#         print("Not enough elements")
#         return

#     print(tup[-4])


# fourthElementFromLast((1, 2, 3))
# fourthElementFromLast((54, 14, 71, 85, 44))
