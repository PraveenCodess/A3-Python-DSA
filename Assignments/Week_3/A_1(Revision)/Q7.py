# . Write a function that returns the string "something" joined with a
# space " " and the given argument a.
# Examples:
# give_me_something("is better than nothing") ➞ "something is better
# than nothing"
# give_me_something("Bob Jane") ➞ "something Bob Jane"
# give_me_something("something") ➞ "something something"


def ret(n):
    return f"Something " + n


n = input()
print(ret(n))
