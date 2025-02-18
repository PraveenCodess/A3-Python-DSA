# . Make two lists of same length and pass it to a function. Return a third
# list where each element is the sum of index.


def func(l1, l2):
    l3 = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            if i == j:
                l3.append(l1[i] + l2[j])

    print(l3)


l1 = [10, 25, 30, -10, 1, 9]
l2 = [58, 11, -15, 20, 6, 1]
func(l1, l2)


# from typing import List


# def addition(lst1: List[int], lst2: List[int]) -> List[int]:
#     result = []

#     # As we know the length are same, we will iterate via index
#     for i in range(0, len(lst1)):
#         result.append(lst1[i] + lst2[i])

#     return result


# my_list1 = [43, 11, 92, 22]
# my_list2 = [-100, -200, 221, 100]

# x = addition(my_list1, my_list2)
# print(x)
