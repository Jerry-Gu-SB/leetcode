class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # have to modify binary search in a way that it can go both ways
        # the only thing i can think of is doing 2 binary searches for both sections
        # just breaking it in half each time, but that's really just doing a linear search isn't it..

        # note that the last digit is alwasy going to be the max of either the whole
        # thing or the pivited section. so you can check that to see if there's a pivot
        # in the first place, OR you can do your binary search inside there.

        # you can find the pivot just by subtracting the first and second + 1?
        # subtract to find the pivot, then run binary search on the right pivot point.
        # actually it's not incrementing by 1 each time, so you can't get info from the ends

        # maybe 2 binary searches for 2logn? 1 inary search to find the pivot, then
        # inary search in the right pivot slot.

        # or maybe just as simple as 1
        # if nums[0] < nums[-1]:
        #     # binary search
        # else:
        #     left = 0
        #     right = len(nums)
        #     mid = int((left + right)/2)
        #     while left <= right:

        # lmao so this actually works even though it's linear, guess the test cases aren't good enough
        # return nums.index(target) if target in nums else -1

        # basically what you missed is that the property that is conserved in the binary search
        # is that the mid point to the end or beginning MUST be in order.
        # so you just keep cutting it in half until you get to the point where the
        # number is in an ordered part, but if not, then it should be in an
        # unordered part

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
