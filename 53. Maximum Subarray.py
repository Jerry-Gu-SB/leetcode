class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # kadane's algorithm. this was kind of what i was getting at before,
        # convince yourself this works

        # also do it using the sliding window method, the dynamic progrmaming method,
        # and the divide and conquer method. we're gonna be doing this problem
        # for a hot minute

        # also you were trying to intuit the sliding window. you need to do more
        # sliding window problems because you aren't recognizing that pattern.
        if not nums: return []

        cur = 0
        solution = -inf
        for num in nums:
            cur = max(num, cur + num)
            solution = max(solution, cur)

        return solution
