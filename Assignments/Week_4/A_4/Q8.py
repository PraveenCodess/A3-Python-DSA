# Ask a string from user. Print the string with first 2 letters and last 2
# letters.
# Example string: aeroplane
# Output: aene
# If length is less than 3, print “INVALID”


s = input()
if len(s) < 4:
    print("Invalid")
else:
    f = s[:2]
    e = s[-2:]
    print(f + e)
