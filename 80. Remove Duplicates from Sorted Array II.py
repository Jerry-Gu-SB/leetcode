class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k

        # okay if the problem was to do what it actually seemed like it's doing this works at least fo rthe test case 1 lol idk
#         if len(nums) <= 2:
#             return nums
#         solution = 0
#         pointer = 0
#         cur = nums[0]
#         count = 1
#         while pointer < len(nums):
#             # print(nums)
#             # print("pointer:", pointer, "cur:", cur, "count:", count)
#             if nums[pointer] == cur:
#                 if count >= 3:
#                     nums.pop(pointer)
#                     cur = nums[pointer]
#                     count = 1
#                     nums.append(0)
#                 else:
#                     count += 1
#                     pointer += 1
#             else:
#                 pointer += 1
#                 cur = nums[pointer]
#                 count = 0
#                 solution += 1
#         return solution