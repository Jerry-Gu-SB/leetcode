class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # xd
        # return target in nums

        # i'm not quite sure what test case it would change here
        # [1,0,1,1,1] target = 0
        # this is the testcase that changes here

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # i originially had these like this but i concinved myself that a while loop would do the same thing
            # but IT DOESN'T.
            if nums[mid] == nums[left]:
                left += 1
                continue
            if nums[mid] == nums[right]:
                right -= 1
                continue

            if nums[left] <= nums[mid]:  # left sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:  # right side sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
