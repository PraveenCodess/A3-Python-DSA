# arr = [56, 2, 76, 32, 65, 89, 32, 78, 11]
# # 8
# x = 32
# # for i in range(0, len(arr)):
# #     if arr[i] == x:
# #         arr.pop(i)
# for num in arr:
#     if num == x:
#         arr.remove(num)
# print(arr)


arr = [56, 2, 76, 32, 32, 32, 65, 89, 32, 78, 32, 32]
result = []
x = 32
for num in arr:
    if num != x:
        result.append(num)
print(result)
