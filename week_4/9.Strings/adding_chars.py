# """
# Enter character = d
# Enter character = t
# Enter character = o
# Enter character = 9
# Enter character = (
# Enter character = q
# """
# a = "anirudh"
# print(id(a))
# a = a + "khurana"
# print(id(a))
# a += "xyz"
# print(id(a))
# print(a)


"""
Enter character = d
Enter character = t
Enter character = o
Enter character = 9
Enter character = (
Enter character = q
"""
# result = ""
result = str()
while True:
    xyz = input("Enter a character = ")
    # if xyz == "q" or xyz == "Q":
    if xyz in ["q", "Q"]:
        break
    result += xyz
print(result)
