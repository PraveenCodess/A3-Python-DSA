#  Ask 5 integers from user. Then ask a single character from user. Print
# those integers separated by that character entered by user.


n = int(input())
l = []
for i in range(1, n + 1):
    val = int(input(f"Enter a number {i} ="))
    l.append(str(val))
chr = input("Enter a character = ")
print(chr.join(l))
