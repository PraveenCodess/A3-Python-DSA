# Keep asking characters from user until he presses q on the keyboard.
# Change all the capital letters to small, and all the small letters to capital.

s = ""
while True:
    n = input()
    if n.isalpha():
        if n.islower():
            n = n.upper()
        else:
            n = n.lower()
    s = s + n
    if n == "q" or n == "Q":
        break

print(s)
