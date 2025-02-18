# Create a function that takes a list of numbers and returns the number
# that's unique.
# Examples
# unique([3, 3, 3, 7, 3, 3]) ➞ 7
# unique([0, 0, 0.77, 0, 0]) ➞ 0.77
# unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0


# def unique(l1):
#     for i in l1:
#         if l1.count(i) == 1:
#             print(i)


# l1 = [0, 1, 1, 1, 1, 1, 1, 1]
# unique(l1)


def count(l1):
    for i in l1:
        c = 0
        x = i
        for j in l1:
            if x == j:
                c += 1
        if c == 1:
            print(x)


l1 = [0, 1, 1, 1, 1, 1, 1, 1]
count(l1)


# def unique(numbers):
#     # Check each number in the list
#     for i in range(len(numbers)):
#         # Assume the current number is unique
#         is_unique = True

#         # Compare it against all other numbers
#         for j in range(len(numbers)):
#             if i != j and numbers[i] == numbers[j]:
#                 is_unique = False
#                 break

#         # If no duplicates were found, this number is unique
#         if is_unique:
#             return numbers[i]


# # Testing the function with examples
# print(unique([3, 3, 3, 7, 3, 3]))  # ➞ 7
# print(unique([0, 0, 0.77, 0, 0]))  # ➞ 0.77
# print(unique([0, 1, 1, 1, 1, 1, 1, 1]))  # ➞ 0
