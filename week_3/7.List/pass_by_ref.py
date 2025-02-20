# Pass by reference, (address)
# Mutable
from typing import List


def change(my_list: List):
    print(f"Mylist = {id(my_list)}")
    my_list[0] = 100


xyz = [34, 22, 11, 78, 67, 65]
print(f"XYZ = {id(xyz)}")
change(xyz)
print(xyz)
