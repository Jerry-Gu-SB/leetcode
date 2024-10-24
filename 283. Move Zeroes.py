class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # manipulating list
        # zeroes = 0
        # for i, num in enumerate(nums):
        #     if num == 0:
        #         zeroes += 1
        # for index in range(zeroes):
        #     nums.remove(0)
        # nums.extend([0 for x in range(zeroes)])


        # better way 2 pointer

        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        return nums
