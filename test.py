# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# print(min(l))


# n = int(input())
# l1 = list(map(int, input().split(" ")))
# l2 = [x for x in l1 if x > 0]
# if len(l2) % 2 != 0:
#     print(l2[len(l2) // 2])
# else:
#     print(l2[(len(l2) // 2) - 1


# l1 = list(map(int, input().split(" ")))
# l2 = [x for x in l1 if x < 0]
# print(sum(l2))


# n = int(input())
# l = list(map(int, input().split(" ")))
# k = int(input())
# temp = []
# for i in range(-1, -k - 1, -1):
#     temp.append(l[i])
#     l.pop(i)
# temp.reverse()
# temp.extend(l)
# print(temp)


# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         n = len(nums)
#         k %= n
#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)

#     def reverse(self, nums: list[int], start: int, end: int) -> None:
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1


n = int(input())
l = list(map(int, input().split()))
k = int(input())

# Take the last k elements
temp = l[-k:]

# Remove the last k elements from the original list
l = l[:-k]

# Combine reversed temp with the rest of the list
temp.reverse()
temp.extend(l)

# Print the result
print(temp)


#         self.reverse(nums, 0, n - 1)
#         self.reverse(nums, 0, k - 1)
#         self.reverse(nums, k, n - 1)

#     def reverse(self, nums: list[int], start: int, end: int) -> None:
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start += 1
#             end -= 1
