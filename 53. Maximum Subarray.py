class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm. this was kind of what i was getting at before,
        # convince yourself this works

        # also do it using the sliding window method, the dynamic progrmaming method,
        # and the divide and conquer method. we're gonna be doing this problem
        # for a hot minute

        # dynamic programming:
        # find the work you have to do
        # find a way to store the work youve already done

        # checking every subarray is just the smaller subarray plus an extra character
        # so if you check 12345, when you check 1, 12, 123, 1234, 12345, you can recursively
        # check 23, 234, 2345 as well and then memoize for next iteration

        grid = [[] for i in len(nums)]
        for i in range(len(nums)):

    # also you were trying to intuit the sliding window. you need to do more
    # sliding window problems because you aren't recognizing that pattern.
    # if not nums: return []

    # cur = 0
    # solution = -inf
    # for num in nums:
    #     cur = max(num, cur + num)
    #     solution = max(solution, cur)

    # return solution
