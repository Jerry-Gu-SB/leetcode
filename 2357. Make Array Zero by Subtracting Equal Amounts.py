class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # one peration?
        # so CHOOSE an integer that's less than the smallest integer > 0
        # then subtract that integer from every element
        # return the min OPERATIONS to make every element zero

        # uhhh this feels like a DP kinda problem honestly

        # so you can choose only 1
        # it feels like yoiu can just greedily pick the biggest number instead of DP actually?
        solution = 0
        while sum(nums) > 0:
            temp_min = float("inf")
            for num in nums:
                if num > 0:
                    temp_min = min(num, temp_min)
            for i, val in enumerate(nums):
                if val > 0:
                    nums[i] -= temp_min
            solution += 1

        return solution

        # i was correct yippeee