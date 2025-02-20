# # Ask a string from user. Print how many characters are there which are
# # not alphabets.
# # Example 1: abc%$#gyhy
# # Output: 3
# # Example 2: AB788&*(^%&*%^&aaaa
# # Output: 13
# # Example 3: 1233^&*(* 0000011
# # Output: 22
# # Example 4: abcdABCD
# Output: 0


def func(s):
    c = 0
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90 or val >= 97 and val <= 122:
            pass
        else:
            c += 1
    print(c)


s = input()
func(s)

# def countNotAlphabets(string: str) -> int:
#     # Method 1
#     """
#     count = 0
#     for ch in string:
#         if not ch.isalpha():
#             count += 1
#     return count
#     """

#     new_string = string.lower()
#     count = 0

#     for ch in new_string:
#         ascii_code = ord(ch)
#         if not (ascii_code >= 97 and ascii_code <= 122):
#             count += 1

#     return count


# print(countNotAlphabets("a bv ^&*"))
