class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # i guess you cna just do a binary search for the initial target, then just do a linear search after to get the range?

        # binary search

        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2

        index = None

        while left <= right:
            # print("left:", left, "middle:", middle, "right:", right)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                index = middle
                break  # so now we've found the index of at least one fo the targets
            middle = (left + right) // 2

        if index == None:
            return [-1, -1]

        # now linear search both ways to find range with 2 pointers

        left = index
        right = index
        print(index)
        while right < len(nums) - 1:
            if nums[right + 1] == target:
                right += 1
            else:
                break

        while left > 0:
            if nums[left - 1] == target:
                left -= 1
            else:
                break

        return [left, right]