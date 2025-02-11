class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        # find the position where it exists or it like would

        # you're either in the middle of like the target, or you're bigger or smaller
        left, middle, right = 0, len(nums) // 2, len(nums) - 1

        while left <= right:
            cur = nums[middle]
            if target <= cur:
                right = middle - 1
            elif target > cur:
                left = middle + 1
            else:
                return middle
            middle = (left + right) // 2

        return left
