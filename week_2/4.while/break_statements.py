# break -> Exit from loop
# return -> Exit from function


# # Break, Continue -> LOOPS
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#     if i == 5:
#         break

# print("Done1")
# print("Done2")


# Break, Continue -> LOOPS
def pattern() -> None:
    i = 1
    while i <= 10:
        print(i)
        if i == 5:
            break
        i += 1
    print("Done1")
    print("Done2")


pattern()
