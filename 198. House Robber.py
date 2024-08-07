class Solution:
    def rob(self, nums: List[int]) -> int:
        # this is pretty simliar to partition equal sum. i think it will be something similar
        # where you're gonna have to add like the current number and not the current sum, but you'll also have to add the adjacent number you skipped.
        # it's just not immediately obvious how you break down teh sub problems because it feels like there's just a lot here.
        # top down, picking YES means that the array is just the same thing except the number at index i and i + 1
        # pickign NO to an element means the array is now just the same thing except index i

        # this is basically maximum subarray except the numbers are all positive, and you can't do adjacent ones
        # if you break it down into a subproblem of length 4 then there are only 3 possiblities. if you break it down to length 3 and 2 there are only 2 possibilities.

        # yeah gonna have to think about it some more.
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        if len(nums) == 3: return max(nums[0] + nums[2], nums[1])
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        dp.append(max(nums[0] + nums[2], nums[1]))

        for i in range(3, len(nums)):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))
        return dp[len(nums) - 1]



