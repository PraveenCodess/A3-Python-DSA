char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"
"""
Capital letters = 
Small letters = 
Digits = 
Spaces = 
Symbols = 
"""
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for i in char:
    val = ord(i)
    if val >= 65 and val <= 90:
        count1 += 1
    elif val >= 97 and val <= 122:
        count2 += 1
    elif val >= 48 and val <= 57:
        count3 += 1
    elif val == 32:
        count4 += 1
    else:
        count5 += 1

print(count1)
print(count2)
print(count3)
print(count4)
print(count5)


# char = "Hhj438&*&$*#(     AHWUuda121&*(^$#*&))"

# """
# Capital letters = 5
# Small letters = 5
# Digits = 6
# Spaces = 5
# Symbols = 17
# """
# cap_letter, small_letter, digits, spaces, symbols = 0, 0, 0, 0, 0
# for ch in char:
#     ascii_code = ord(ch)
#     if ascii_code >= 65 and ascii_code <= 90:
#         cap_letter += 1
#     elif ascii_code >= 97 and ascii_code <= 122:
#         small_letter += 1
#     elif ascii_code >= 48 and ascii_code <= 57:
#         digits += 1
#     elif ascii_code == 32:
#         spaces += 1
#     else:
#         symbols += 1
# print(cap_letter, small_letter, digits, spaces, symbols)
