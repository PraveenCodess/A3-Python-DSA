# Create a function that takes damage and speed (attacks per second)
# and returns the amount of damage after a given time.
# Examples:
# damage(40, 5, "second") ➞ 200
# damage(100, 1, "minute") ➞ 6000
# damage(2, 100, "hour") ➞ 720000
# Return "invalid" if damage or speed is negative


def attack(d, s, t):
    if d < 0 or s < 0:
        print("Invalid")
        return
    if t == "second":
        print(d * s)
    elif t == "minute":
        print(d * s * 60)
    elif t == "hour":
        print(d * s * 60 * 60)
    else:
        print("Speify the mode of Time Correctly")


d, s = map(int, input().split(","))
t = input()
attack(d, s, t)
